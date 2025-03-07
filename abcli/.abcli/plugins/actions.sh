#! /usr/bin/env bash

function abcli_perform_action() {
    local options=$1
    local action_name=$(abcli_option "$options" action void)
    local plugin_name=$(abcli_option "$options" plugin abcli)

    local function_name=${plugin_name}_action_${action_name}

    [[ $(type -t $function_name) != "function" ]] &&
        return 0

    abcli_log "✴️  action: $plugin_name: $action_name."
    $function_name "${@:2}"
}

function abcli_action_git_before_push() {
    abcli build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "current" ]] &&
        return 0

    abcli pypi build
}
