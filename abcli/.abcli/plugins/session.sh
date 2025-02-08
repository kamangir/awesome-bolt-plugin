#! /usr/bin/env bash

function abcli_session() {
    local task=$(abcli_unpack_keyword $1 start)

    if [ $task == "start" ]; then
        local options=$2

        local do_pull=1
        [[ "$abcli_is_mac" == true ]] && do_pull=0
        do_pull=$(abcli_option_int "$options" pull $do_pull)

        abcli_log "session started: $options ${@:3}"

        while true; do
            [[ "$do_pull" == 1 ]] &&
                abcli_git_pull init

            abcli_log "session initialized: username=$USER, hostname=$(hostname), EUID=$EUID, python3=$(which python3)"

            if [[ "$abcli_is_mac" == false ]]; then
                sudo rm -v $ABCLI_PATH_IGNORE/session_reply_*
                abcli_storage clear
            else
                rm -v $ABCLI_PATH_IGNORE/session_reply_*
            fi

            local plugin_name=$BLUE_SBC_SESSION_PLUGIN
            local function_name=${plugin_name}_session
            if [[ $(type -t $function_name) == "function" ]]; then
                $function_name start "${@:3}"
            else
                if [ -z "$plugin_name" ]; then
                    abcli_log_warning "@session: plugin not found."
                else
                    abcli_log_error "@session: plugin: $plugin_name: plugin not found."
                fi
                abcli_sleep seconds=60
            fi

            abcli_log "session closed."

            if [ -f "$ABCLI_PATH_IGNORE/session_reply_exit" ]; then
                abcli_log "abcli.reply_to_bash(exit)"
                return
            fi

            if [ -f "$ABCLI_PATH_IGNORE/session_reply_reboot" ]; then
                abcli_log "abcli.reply_to_bash(reboot)"
                abcli_host reboot
            fi

            if [ -f "$ABCLI_PATH_IGNORE/session_reply_seed" ]; then
                abcli_log "abcli.reply_to_bash(seed)"

                abcli_git_pull
                abcli_init

                cat "$ABCLI_PATH_IGNORE/session_reply_seed" | while read line; do
                    abcli_log "executing: $line"
                    eval $line
                done
            fi

            if [ -f "$ABCLI_PATH_IGNORE/session_reply_shutdown" ]; then
                abcli_host shutdown
            fi

            if [ -f "$ABCLI_PATH_IGNORE/session_reply_update" ]; then
                abcli_log "abcli.reply_to_bash(update)"
            fi

            if [ -f "$ABCLI_PATH_IGNORE/disabled" ]; then
                abcli_log "abcli is disabled."
                return
            fi

            abcli_sleep seconds=5
        done

        return
    fi

    abcli_log_error "@session: $task: command not found."
    return 1
}
