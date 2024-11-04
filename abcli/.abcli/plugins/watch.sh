#! /usr/bin/env bash

function abcli_watch() {
    local options=$1
    local do_clear=$(abcli_option_int "$options" clear 1)

    local command_line="${@:2}"

    abcli_log "watching $command_line ..."

    while true; do
        [[ "$do_clear" == 1 ]] && clear

        abcli_eval ,$options "$command_line"

        abcli_sleep ,$options
    done
}
