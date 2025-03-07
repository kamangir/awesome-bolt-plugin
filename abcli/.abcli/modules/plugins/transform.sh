#! /usr/bin/env bash

function abcli_plugins_transform() {
    local repo_name=$1
    if [[ -z "$repo_name" ]]; then
        abcli_log_error "@plugins: transform: $repo_name: repo not found."
        return 1
    fi
    local plugin_name=$(abcli_plugin_name_from_repo $repo_name)

    abcli_log "blue-plugin -> $repo_name ($plugin_name)"

    pushd $abcli_path_git/$repo_name >/dev/null

    git mv blue_plugin $plugin_name

    git mv \
        $plugin_name/.abcli/blue_plugin.sh \
        $plugin_name/.abcli/$plugin_name.sh

    rm -v $plugin_name/.abcli/session.sh

    python3 -m abcli.plugins \
        transform \
        --repo_name $repo_name \
        --plugin_name $plugin_name \
        "${@:2}"
}
