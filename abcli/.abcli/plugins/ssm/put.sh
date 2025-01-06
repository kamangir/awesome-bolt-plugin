#! /usr/bin/env bash

function abcli_ssm_put() {
    local options=$1

    local secret_name
    local secret_value

    local verbose=$(abcli_option_int "$options" verbose 0)
    local plugin_name=$(abcli_option "$options" plugin)
    local repo_name=""
    [[ ! -z "$plugin_name" ]] &&
        repo_name=$(abcli_unpack_repo_name $plugin_name)
    repo_name=$(abcli_option "$options" repo $repo_name)
    if [[ ! -z "$repo_name" ]]; then
        pushd $abcli_path_git/$repo_name >/dev/null
        local line
        local count=0
        for line in $(dotenv \
            --file .env \
            list \
            --format shell); do
            [[ $verbose == 1 ]] && abcli_log "$line"

            secret_name=$(python3 -c "print('$line'.split('=',1)[0])")
            secret_value=$(python3 -c "print('$line'.split('=',1)[1])")

            abcli_ssm put $secret_name $secret_value

            ((count++))
        done
        popd >/dev/null

        abcli_log "@ssm: put: $repo_name/.env: $count secret(s)"
        return
    fi

    secret_name=$1
    if [[ -z "$secret_name" ]]; then
        abcli_log_error "@ssm: put: name not found."
        return 1
    fi

    secret_value=$2
    if [[ -z "$secret_value" ]]; then
        abcli_log_error "@ssm: put: value not found."
        return 1
    fi

    python3 -m abcli.plugins.ssm \
        put \
        --name "$secret_name" \
        --value "$secret_value" \
        "${@:3}"
}
