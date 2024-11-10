#! /usr/bin/env bash

function abcli_pypi_browse() {
    local options=$1
    local plugin_name=$(abcli_option "$options" plugin abcli)
    local do_token=$(abcli_option_int "$options" token 0)

    local module_name=$(abcli_get_module_name_from_plugin $plugin_name)

    local url="https://pypi.org/project/$module_name/"
    [[ "$do_token" == 1 ]] &&
        url="https://pypi.org/manage/account/token/"

    abcli_browse $url

    [[ "$do_token" == 0 ]] && return 0

    local pyrc_filename=$HOME/.pypirc
    [[ ! -f "$pyrc_filename" ]] &&
        cp -v \
            $abcli_path_assets/pypi/.pypirc \
            $pyrc_filename

    nano $pyrc_filename
}
