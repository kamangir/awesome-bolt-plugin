#! /usr/bin/env bash

function abcli_conda_list() {
    abcli_eval ,$1 \
        conda info \
        --envs "${@:2}"
}
