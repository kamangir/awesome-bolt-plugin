#! /usr/bin/env bash

function abcli_latex() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=abcli_latex_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@latex: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /latex
