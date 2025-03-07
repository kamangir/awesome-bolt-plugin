#! /usr/bin/env bash

function abcli_gpu() {
    local task=$(abcli_unpack_keyword $1 status)

    local function_name=abcli_gpu_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ $task == "validate" ]; then
        abcli_log $(python3 -m abcli.plugins.gpu validate)
        return
    fi

    abcli_log_error "@gpu: $task: command not found."
    return 1
}

function abcli_gpu_status() {
    local task=$(abcli_unpack_keyword $1 show)

    if [ $task == "get" ]; then
        local options=$2
        local from_cache=$(abcli_option_int "$options" from_cache 1)

        local status=""
        [[ "$from_cache" == 1 ]] &&
            local status=$abcli_gpu_status_cache

        [[ -z "$status" ]] &&
            local status=$(python3 -m abcli.plugins.gpu \
                status \
                "${@:3}")

        export abcli_gpu_status_cache=$status

        $abcli_gpu_status_cache && local message="found. ✅" || local message='not found.'
        abcli_log "🔋 gpu: $message"
        return
    fi

    if [ $task == "show" ]; then
        abcli_eval - nvidia-smi

        abcli_log "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"

        abcli_gpu_status get

        abcli_gpu validate

        return
    fi

    abcli_log_error "@gpu: status: $task: command not found."
    return 1
}

abcli_gpu_status get
$abcli_gpu_status_cache && export abcli_status_icons="🔋 $abcli_status_icons"
