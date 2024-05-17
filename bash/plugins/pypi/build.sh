#! /usr/bin/env bash

function abcli_pypi_build() {
    local options=$1

    local plugin_name=$(abcli_option "$options" plugin abcli)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="${EOP}install,${EOPE}upload"
        [[ "$plugin_name" == abcli ]] && options="$options$EOP,plugin=<plugin-name>$EOPE"
        abcli_show_usage "@pypi build$ABCUL$options" \
            "build $plugin_name for pypi."
        return
    fi

    local do_install=$(abcli_option_int "$options" install 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    if [[ "$do_install" == 1 ]]; then
        pip3 install setuptools wheel twine
        python3 -m pip install --upgrade build
    fi

    local repo_name=$(abcli_unpack_repo_name $plugin_name)
    if [[ ! -d "$abcli_path_git/$repo_name" ]]; then
        abcli_log "-@pypi: build: $repo_name: repo not found."
        return 1
    fi

    abcli_log "pypi: building $plugin_name ($repo_name)..."

    pushd $abcli_path_git/$repo_name >/dev/null
    python3 -m build
    [[ "$do_upload" == 1 ]] &&
        twine upload dist/*
    popd >/dev/null

    return 0
}
