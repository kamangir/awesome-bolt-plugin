#! /usr/bin/env bash

function abcli_pytest() {
    local options=$1

    local plugin_name=$(abcli_option "$options" plugin abcli)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,list,~log,plugin=<plugin-name>"
        abcli_show_usage "$plugin_name pytest$ABCUL[$options]$ABCUL[args]" \
            "pytest $plugin_name."
        return
    fi

    local args="${@:2}"

    [[ $(abcli_option_int "$options" list 0) == 1 ]] &&
        local args="--collect-only"

    abcli_eval "path=$abcli_path_git/$plugin_name,$options" \
        pytest "$args"
}
