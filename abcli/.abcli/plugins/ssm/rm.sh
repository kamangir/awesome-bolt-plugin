#! /usr/bin/env bash

function abcli_ssm_rm() {
    python3 -m abcli.plugins.ssm \
        rm \
        --name "$1" \
        "${@:2}"
}
