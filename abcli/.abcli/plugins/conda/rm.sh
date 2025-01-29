#! /usr/bin/env bash

function abcli_conda_rm() {
    local options=$1
    local environment_name=$(abcli_option "$options" name abcli)

    local exists=$(abcli_conda_exists name=$environment_name)
    if [[ "$exists" == 0 ]]; then
        abcli_log_warning "@conda: $environment_name does not exist."
        return 0
    fi

    conda activate base
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        conda remove -y \
        --name $environment_name \
        --all
}
