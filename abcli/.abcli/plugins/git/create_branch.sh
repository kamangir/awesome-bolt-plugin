#! /usr/bin/env bash

function abcli_git_create_branch() {
    local branch_name=$1
    if [[ -z "$branch_name" ]]; then
        abcli_log_error "@git: create_brach: branch name not found."
        return 1
    fi

    local options=$2
    local do_push=$(abcli_option_int "$options" push 1)
    local do_increment_version=$(abcli_option_int "$options" increment_version $(abcli_not $do_push))
    local do_timestamp=$(abcli_option_int "$options" timestamp 1)

    if [[ "$do_increment_version" == 1 ]]; then
        abcli_git_increment_version
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_timestamp" == 1 ]] &&
        branch_name=$branch_name-$(abcli_string_timestamp_short)

    git pull
    [[ $? -ne 0 ]] && return 1

    git checkout -b $branch_name
    [[ $? -ne 0 ]] && return 1

    git push origin $branch_name
    [[ $? -ne 0 ]] && return 1

    if [[ "$do_push" == 1 ]]; then
        abcli_git_push "start of $branch_name 🪄" first
    fi
}
