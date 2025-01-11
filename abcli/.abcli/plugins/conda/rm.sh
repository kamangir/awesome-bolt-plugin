#! /usr/bin/env bash

function abcli_conda_rm() {
    local options=$1
    local environment_name=$(abcli_option "$options" name abcli)

    conda activate base
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        conda remove -y \
        --name $environment_name \
        --all
}
