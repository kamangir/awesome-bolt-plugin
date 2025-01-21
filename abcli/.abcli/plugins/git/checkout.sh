#! /usr/bin/env bash

function abcli_git_checkout() {
    local thing=$1

    if [[ -z "$thing" ]]; then
        abcli_log_error "@git: checkout: args not found."
        return 1
    fi

    local options=$2
    local do_fetch=$(abcli_option_int "$options" fetch 1)
    local do_pull=$(abcli_option_int "$options" pull 1)
    local do_rebuild=$(abcli_option_int "$options" rebuild 0)

    if [[ "$do_fetch" == 1 ]]; then
        git fetch
        [[ $? -ne 0 ]] && return 1
    fi

    git checkout \
        "$thing" \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    if [[ "$do_pull" == 1 ]]; then
        git pull
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_rebuild" == 1 ]]; then
        abcli_git_push "rebuild"
    fi
}
