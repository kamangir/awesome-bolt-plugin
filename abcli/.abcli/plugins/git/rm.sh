#! /usr/bin/env bash

function abcli_git_rm() {
    local repo_name=${1:-void}

    if [[ ! -d "$abcli_path_git/$repo_name" ]]; then
        abcli_log_error "$repo_name: repo not found."
        return 1
    fi

    local plugin_name=$(abcli_plugin_name_from_repo $repo_name)
    abcli_log "removing repo: $repo_name == plugin_name: $plugin_name"

    pip3 uninstall -y $plugin_name

    rm -rfv "$abcli_path_git/$repo_name"
}
