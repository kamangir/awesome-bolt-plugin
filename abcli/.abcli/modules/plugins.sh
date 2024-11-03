#! /usr/bin/env bash

function abcli_plugins() {
    local task=$(abcli_unpack_keyword "$1")

    local function_name="abcli_plugins_$1"
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ $task == "get_module_name" ]; then
        python3 -m abcli.plugins \
            get_module_name \
            --repo_name "$2" \
            "${@:3}"
        return
    fi

    if [ $task == "list_of_external" ]; then
        python3 -m abcli.plugins \
            list_of_external \
            "${@:2}"
        return
    fi

    python3 -m abcli.plugins "$task" "${@:2}"
}

abcli_source_caller_suffix_path /plugins
