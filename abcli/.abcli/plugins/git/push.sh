#! /usr/bin/env bash

function abcli_git_push() {
    local message=$1
    if [[ -z "$message" ]]; then
        abcli_log_error "@git: push: message not found."
        return 1
    fi

    local options=$2
    local do_browse=$(abcli_option_int "$options" browse 0)
    local do_increment_version=$(abcli_option_int "$options" increment_version 1)
    local show_status=$(abcli_option_int "$options" status 1)
    local first_push=$(abcli_option_int "$options" first 0)
    local create_pull_request=$(abcli_option_int "$options" create_pull_request $first_push)
    local do_action=$(abcli_option_int "$options" action 1)
    local run_workflows=$(abcli_option_int "$options" workflow 1)

    if [[ "$do_increment_version" == 1 ]]; then
        abcli_git_increment_version
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$show_status" == 1 ]] &&
        git status

    local repo_name=$(abcli_git_get_repo_name)
    local plugin_name=$(abcli_plugin_name_from_repo $repo_name)

    if [[ "$do_action" == 1 ]]; then
        abcli_perform_action \
            action=git_before_push,plugin=$plugin_name
        if [[ $? -ne 0 ]]; then
            abcli_log_error "@git: push: action failed."
            return 1
        fi
    fi

    git add .
    [[ $? -ne 0 ]] && return 1

    message="$message - kamangir/bolt#746"
    [[ "$run_workflows" == 0 ]] &&
        message="$message - no-workflow 🪄"

    git commit -a -m "$message"
    [[ $? -ne 0 ]] && return 1

    local extra_args=""
    [[ "$first_push" == 1 ]] &&
        extra_args="--set-upstream origin $(abcli_git get_branch)"

    git push $extra_args
    [[ $? -ne 0 ]] && return 1

    if [[ "$create_pull_request" == 1 ]]; then
        abcli_git create_pull_request
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_browse" == 1 ]] &&
        abcli_git_browse . actions

    local build_options=$3
    if [[ $(abcli_option_int "$build_options" build 0) == 1 ]]; then
        abcli_pypi_build $build_options,plugin=$plugin_name
    fi
}
