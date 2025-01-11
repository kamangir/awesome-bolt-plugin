#! /usr/bin/env bash

function abcli_conda_exists() {
    local options=$1
    local environment_name=$(abcli_option "$options" name abcli)

    if conda info --envs | grep -q "^$environment_name "; then
        echo 1
    else
        echo 0
    fi
}
