#! /usr/bin/env bash

function abcli_ssm_get() {
    local options=$1

    local secret_name
    local secret_value

    local path=$(abcli_option "$options" path)
    if [[ ! -z "$path" ]]; then
        if [[ ! -f "$path/sample.env" ]]; then
            abcli_log_warning "@ssm: get: $path/sample.env: file not found."
            return 1
        fi

        pushd $path >/dev/null
        local line
        local count=0
        for line in $(dotenv \
            --file sample.env \
            list \
            --format shell); do

            secret_name=$(python3 -c "print('$line'.split('=',1)[0])")

            secret_value=$(abcli_ssm get $secret_name)

            if [[ -z "$secret_value" ]]; then
                abcli_log "🔑 $secret_name (blank)"
            else
                abcli_log "🔑 $secret_name"
            fi

            export $secret_name=$secret_value

            ((count++))
        done
        popd >/dev/null

        abcli_log "@ssm: get: $count secret(s): $path/sample.env"
        return
    fi

    secret_name=$1

    python3 -m abcli.plugins.ssm \
        get \
        --name "$secret_name" \
        "${@:2}"
}
