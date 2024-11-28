#! /usr/bin/env bash

function test_abcli_list_filter() {
    abcli_assert \
        $(abcli_list_filter this,which,that,who,12 \
            --contains th) \
        this,that
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_filter this,which,that,who,12 \
            --doesnt_contain wh) \
        this,that,12
}

function test_abcli_list_in() {
    abcli_assert \
        $(abcli_list_in that this,that,which) \
        True
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_in who this,that,which) \
        False
}

function test_abcli_list_intersect() {
    abcli_assert_list \
        $(abcli_list_intersect this,that,who which,that,what,this) \
        this,that
}

function test_abcli_list_item() {
    abcli_assert \
        $(abcli_list_item this,that,who 1) \
        that
}

function test_abcli_list_len() {
    abcli_assert \
        $(abcli_list_len this,that,which) \
        3
}

function test_abcli_list_nonempty() {
    abcli_assert \
        $(abcli_list_nonempty this,,that) \
        this,that
}

function test_abcli_list_next() {
    abcli_assert \
        $(abcli_list_next what what,which,this,that,something) \
        which
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_next this what,which,this,that,something) \
        that
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(abcli_list_next something what,which,this,that,something)" \
        - empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(abcli_list_next void what,which,this,that,something)" \
        - empty
}

function test_abcli_list_prev() {
    abcli_assert \
        "$(abcli_list_prev what what,which,this,that,something)" \
        - empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_prev this what,which,this,that,something) \
        which
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_prev something what,which,this,that,something) \
        that
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(abcli_list_prev void what,which,this,that,something)" \
        - empty
}

function test_abcli_list_resize() {
    abcli_assert \
        $(abcli_list_resize this,that,which 2) \
        this,that
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_resize this,that,which -1) \
        this,that,which
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(abcli_list_resize this,that,which 0)" \
        - empty
}

function test_abcli_list_sort() {
    abcli_assert \
        $(abcli_list_sort this,that) \
        that,this
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(abcli_list_sort this,that,this,12,which \
            --unique 1) \
        12,that,this,which
}
