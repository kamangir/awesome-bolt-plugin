#! /usr/bin/env bash

function test_abcli_hr() {
    abcli_hr
}

function test_abcli_log_local() {
    abcli_log_local "testing"
}

function test_abcli_show_usage() {
    abcli_show_usage "command-line" \
        "usage"
}
