#! /usr/bin/env bash

function test_abcli_help() {
    local options=$1

    local module
    for module in \
        "abcli" \
        \
        "abcli git" \
        "abcli git browse" \
        "abcli git checkout" \
        "abcli git clone" \
        "abcli git create_branch" \
        "abcli git create_pull_request" \
        "abcli git get_branch" \
        "abcli git get_repo_name" \
        "abcli git increment_version" \
        "abcli git pull" \
        "abcli git push" \
        "abcli git recreate_ssh" \
        "abcli git reset" \
        "abcli git review" \
        "abcli git status" \
        "abcli git sync_fork"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
