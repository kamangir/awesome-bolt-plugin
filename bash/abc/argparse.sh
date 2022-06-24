#! /usr/bin/env bash

function abc_argparse_get() {
    python3 -m abc.string \
        argparse \
        --list_of_args "$1" \
        --arg "$2" \
        --default "$3" \
        ${@:6}
}

function abc_arg_get() {
    local var="$1"
    local default="$2"

    if [ "$var" == "-" ] ; then
        local var=""
    fi
    if [ ! -z "$default" ] ; then
        if [ -z "$var" ] ; then
            local var=$default
        fi
    fi
    echo $var
}