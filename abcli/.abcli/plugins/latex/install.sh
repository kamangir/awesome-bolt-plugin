#! /usr/bin/env bash

function abcli_latex_install() {
    local options=$1

    if [[ "$abcli_is_mac" == true ]]; then
        abcli_eval ,$options \
            brew install bibclean

        abcli_eval ,$options \
            brew install --cask mactex

        abcli_log_warning "restart the terminal..."
        return
    fi

    abcli_log_error "@latex: build: not supported here."
    return 1
}
