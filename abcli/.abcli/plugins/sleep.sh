#! /usr/bin/env bash

function abcli_sleep() {
    local options=$1
    local seconds=$(abcli_option "$options" seconds 3)

    abcli_log_local "sleeping for $seconds s ... (^C to stop)"
    sleep $seconds
}
