#! /usr/bin/env bash

function test_abcli_help() {
    local options=$1

    local module
    for module in \
        "@badge" \
        \
        "@batch browse" \
        "@batch cat" \
        "@batch eval" \
        "@batch list" \
        "@batch submit" \
        \
        "@browse" \
        \
        "@cat" \
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
        "@env" \
        "@env backup" \
        "@env backup list" \
        "@env dot" \
        "@env dot cat" \
        "@env dot cat" \
        "@env dot cp" \
        "@env dot edit" \
        "@env dot get" \
        "@env dot list" \
        "@env dot load" \
        "@env dot set" \
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
        "@pause" \
        \
        "@plugins get_module_name" \
        "@plugins install" \
        "@plugins list_of_external" \
        "@plugins list_of_installed" \
        "@plugins transform" \
        \
        "@pylint" \
        \
        "@pypi" \
        "@pypi browse" \
        "@pypi build" \
        "@pypi install" \
        \
        "@pytest" \
        \
        "@repeat" \
        \
        "@seed" \
        "@seed eject" \
        "@seed list" \
        \
        "@sleep" \
        \
        "@test" \
        "@test list" \
        \
        "@terraform" \
        "@terraform cat" \
        "@terraform disable" \
        "@terraform enable" \
        \
        "@watch" \
        \
        "abcli_log_list" \
        "abcli_source_caller_suffix_path" \
        "abcli_source_path" \
        \
        "abcli"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
