#! /usr/bin/env bash

function abcli_conda() {
    local task=$(abcli_unpack_keyword $1)

    local function_name="abcli_conda_$task"
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    conda "$@"
}

abcli_source_caller_suffix_path /conda
