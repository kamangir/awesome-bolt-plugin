#! /usr/bin/env bash

function test_abcli_help() {
    local options=$1

    local module
    for module in \
        "@git" \
        "@git browse" \
        "@git checkout" \
        "@git clone" \
        "@git create_branch" \
        "@git create_pull_request" \
        "@git get_branch" \
        "@git get_repo_name" \
        "@git increment_version" \
        "@git pull" \
        "@git push" \
        "@git recreate_ssh" \
        "@git reset" \
        "@git review" \
        "@git status" \
        "@git sync_fork" \
        \
        "@gpu status get" \
        "@gpu status show" \
        "@gpu validate" \
        \
        "abcli"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
