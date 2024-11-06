#! /usr/bin/env bash

function test_abcli_repeat() {
    abcli_repeat - ls
    abcli_assert "$?" 0

    abcli_repeat count=3 ls
    abcli_assert "$?" 0
}
