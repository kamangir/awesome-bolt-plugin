#! /usr/bin/env bash

function abcli_latex_build() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_install=$(abcli_option_int "$options" install 0)
    local do_ps=$(abcli_option_int "$options" ps 1)
    local do_pdf=$(abcli_option_int "$options" pdf 1)
    local bib_file=$(abcli_option "$options" bib)

    [[ "$do_install" == 1 ]] &&
        abcli_latex_install $options

    local full_path=$2
    if [[ ! -f "$full_path" ]]; then
        abcli_log_error "@latex: build: $full_path: file not found."
        return 1
    fi
    local path=$(dirname "$full_path")
    local filename=$(basename "$full_path")
    filename=${filename%.*}
    abcli_log "building $path / $filename.tex..."

    pushd $path >/dev/null

    rm -v $filename.dvi
    rm -v $filename.ps

    local round
    for round in 1 2 3; do
        abcli_log "round $round..."

        abcli_eval dryrun=$do_dryrun \
            latex \
            -interaction=nonstopmode \
            $filename.tex
        [[ $? -ne 0 ]] && return 1

        [[ ! -z "$bib_file" ]] &&
            abcli_eval dryrun=$do_dryrun \
                bibtex $bib_file
    done

    #abcli_eval dryrun=$do_dryrun \
    #    makeindex $filename.idx

    [[ "$do_ps" == 1 ]] &&
        abcli_eval dryrun=$do_dryrun \
            dvips \
            -o $filename.ps \
            $filename.dvi

    [[ "$do_pdf" == 1 ]] &&
        abcli_eval dryrun=$do_dryrun \
            ps2pdf $filename.ps

    popd >/dev/null
}
