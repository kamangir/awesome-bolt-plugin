#! /usr/bin/env bash

function abcli_latex_install() {
    if [[ "$abcli_is_mac" == true ]]; then
        brew install bibclean

        brew install --cask mactex

        abcli_log_warning "restart the terminal..."
        return
    fi

    abcli_log_error "@latex: build: not supported here."
    return 1
}
