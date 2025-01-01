#! /usr/bin/env bash

function abcli_latex_bibclean() {
    local options=$1
    local do_install=$(abcli_option_int "$options" install 0)

    [[ "$do_install" == 1 ]] &&
        abcli_latex_install $options

    local filename=${2:-void}

    local temp_filename=$abcli_path_temp/bibclean-$(abcli_string_timestamp_short).bib

    abcli_eval ,$options \
        bibclean $filename >$temp_filename

    mv -v $temp_filename $filename
}
