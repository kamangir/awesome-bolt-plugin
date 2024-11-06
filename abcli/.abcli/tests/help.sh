#! /usr/bin/env bash

function test_abcli_help() {
    local options=$1

    local module
    for module in \
        "@batch browse" \
        "@batch cat" \
        "@batch eval" \
        "@batch list" \
        "@batch submit" \
        \
        "@docker browse " \
        "@docker build " \
        "@docker clear " \
        "@docker eval " \
        "@docker push " \
        "@docker run " \
        "@docker seed " \
        "@docker source " \
        \
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
        "@init" \
        \
        "@latex" \
        "@latex build" \
        "@latex install" \
        \
        "@plugins get_module_name" \
        "@plugins install" \
        "@plugins list_of_external" \
        "@plugins list_of_installed" \
        "@plugins transform" \
        \
        "@repeat" \
        \
        "@sleep" \
        \
        "@terraform" \
        "@terraform cat" \
        "@terraform disable" \
        "@terraform enable" \
        \
        "@watch" \
        \
        "abcli"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
