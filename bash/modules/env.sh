#! /usr/bin/env bash

function abcli_env() {
    local task=$(abcli_unpack_keyword $1)

    if [ "$task" == "help" ]; then
        abcli_show_usage "abcli env [keyword]" \
            "show environment variables [relevant to keyword]."

        abcli_env dot "$@"

        abcli_show_usage "abcli env memory" \
            "show memory status."
        return
    fi

    if [ "$task" == dot ]; then
        local subtask=$2

        if [[ "$subtask" == "help" ]]; then
            abcli_env dot cat "$@"

            abcli_show_usage "abcli env dot cp|copy$ABCUL<env-name>${ABCUL}jetson_nano|rpi$ABCUL<machine-name>" \
                "cp <env-name> to machine."

            abcli_show_usage "abcli env dot edit${ABCUL}jetson_nano|rpi$ABCUL<machine-name>" \
                "edit .env on machine."

            abcli_show_usage "abcli env dot get <variable>" \
                "<variable>."

            abcli_show_usage "abcli env dot load" \
                "load .env."

            abcli_show_usage "abcli env dot list" \
                "list env repo."

            abcli_show_usage "abcli env dot set <variable> <value>" \
                "<variable> = <value>."
            return
        fi

        if [[ "$subtask" == "cat" ]]; then
            local env_name=$(abcli_clarify_input $3 .env)

            if [[ "$env_name" == "help" ]]; then
                abcli_show_usage "abcli env dot cat$ABCUL[|<env-name>|sample]" \
                    "cat .env|<env-name>|sample.env."

                abcli_show_usage "abcli env dot cat${ABCUL}jetson_nano|rpi <machine-name>" \
                    "cat .env from machine."
                return
            fi

            if [[ "$env_name" == ".env" ]]; then
                pushd $abcli_path_abcli >/dev/null
                abcli_eval - \
                    dotenv list --format shell
                popd >/dev/null
                return
            fi

            if [ "$(abcli_list_in $env_name rpi,jetson_nano)" == True ]; then
                local machine_kind=$3
                local machine_name=$4

                local filename="$abcli_path_temp/scp-${machine_kind}-${machine_name}.env"

                abcli_scp \
                    $machine_kind \
                    $machine_name \
                    \~/git/awesome-bash-cli/.env \
                    - \
                    - \
                    $filename

                cat $filename

                return
            fi

            if [[ "$env_name" == "sample" ]]; then
                abcli_eval - \
                    cat $abcli_path_abcli/sample.env
                return
            fi

            abcli_eval - \
                cat $abcli_path_abcli/assets/env/$env_name.env

            return
        fi

        if [[ "|cp|copy|" == *"|$task|"* ]]; then
            local env_name=$3
            local machine_kind=$(abcli_clarify_input $4 local)
            local machine_name=$5

            if [ "$machine_kind" == "local" ]; then
                cp -v \
                    $abcli_path_abcli/assets/env/$env_name.env \
                    $$abcli_path_abcli/.env
            else
                # https://kb.iu.edu/d/agye
                abcli_scp \
                    local \
                    - \
                    $abcli_path_abcli/assets/env/$env_name.env \
                    $machine_kind \
                    $machine_name \
                    \~/git/awesome-bash-cli/.env
            fi

            return
        fi

        if [ "$task" == "edit" ]; then
            local machine_kind=$(abcli_clarify_input $3 local)
            local machine_name=$4

            if [ "$machine_kind" == "local" ]; then
                nano $abcli_path_abcli/.env
            else
                local filename="$abcli_object_temp/scp-${machine_kind}-${machine_name}.env"

                abcli_scp \
                    $machine_kind \
                    $machine_name \
                    \~/git/awesome-bash-cli/.env \
                    - \
                    - \
                    $filename

                nano $filename

                abcli_scp \
                    local \
                    - \
                    $filename \
                    $machine_kind \
                    $machine_name \
                    \~/git/awesome-bash-cli/.env
            fi
            return
        fi

        if [ "$task" == "get" ]; then
            pushd $abcli_path_abcli >/dev/null
            dotenv get "${@:3}"
            popd >/dev/null
            return
        fi

        if [[ "$subtask" == "list" ]]; then
            ls -1lh $abcli_path_abcli/assets/env/*.env
            return
        fi

        if [[ "$subtask" == "load" ]]; then
            pushd $abcli_path_abcli >/dev/null
            local line
            local count=0
            for line in $(dotenv list --format shell); do
                export "$line"
                ((count++))
            done
            popd >/dev/null

            abcli_log "📜 loaded $count variable(s) from $abcli_path_abcli/.env"
            return
        fi

        if [ "$task" == "set" ]; then
            pushd $abcli_path_abcli >/dev/null
            dotenv set "${@:3}"
            popd >/dev/null
            return
        fi

        abcli_log_error "-abcli: $task: $subtask: command not found."
        return 1
    fi

    if [ "$task" == memory ]; then
        grep MemTotal /proc/meminfo
        return
    fi

    env | grep abcli_ | grep "$1" | sort
}

abcli_env dot load
