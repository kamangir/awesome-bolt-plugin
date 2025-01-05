#! /usr/bin/env bash

function abcli_ssm() {
    local task=$1

    local function_name=abcli_ssm_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m abcli.plugins.ssm "$@"
}

abcli_source_caller_suffix_path /ssm

# to get around a pip import issue.
abcli_env_dot_load \
    caller,ssm,plugin=abcli,suffix=/../../..
