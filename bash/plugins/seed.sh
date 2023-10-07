#! /usr/bin/env bash

function abcli_seed() {
    local task=$(abcli_unpack_keyword $1)

    if [ "$task" == "help" ]; then
        abcli_show_usage "abcli seed$ABCUL[.|docker|ec2|jetson|headless_rpi|mac|rpi]$ABCUL[clipboard|filename=<filename>|key|screen]$ABCUL[cookie=<cookie-name>,~log]" \
            "generate and output a seed 🌱."
        abcli_show_usage "abcli seed <target>$ABCUL<args>" \
            "seed 🌱 <target>."
        abcli_show_usage "abcli seed add_file$ABCUL<filename>$ABCUL[output=<output>]" \
            "seed 🌱 += <filename>."
        abcli_show_usage "abcli seed eject" \
            "eject seed 🌱."
        return
    fi

    if [ "$task" == "add_file" ]; then
        local filename=$2

        local options=$3
        local output=$(abcli_option "$options" output "clipboard")

        local sudo_prefix="sudo "
        local delim="\n"
        if [ "$output" == "clipboard" ]; then
            local delim="; "
        fi

        local base64="base64"
        if [ "$abcli_is_ubuntu" == true ]; then
            # https://superuser.com/a/1225139
            local base64="base64 -w 0"
        fi

        local var_name=_abcli_seed_$(echo $filename | tr / _ | tr . _ | tr - _)

        local seed="$var_name=\"$(cat $HOME/$filename | $base64)\"$delim"
        local seed="${seed}echo \$$var_name | base64 --decode > $var_name$delim"
        local seed="$seed${sudo_prefix}mv $var_name \$HOME/$filename"

        echo $seed
        return
    fi

    if [ "$task" == "eject" ]; then
        if [[ "$abcli_is_jetson" == true ]]; then
            sudo eject /media/abcli/SEED
        else
            sudo diskutil umount /Volumes/seed
        fi
        return
    fi

    local target=$(abcli_clarify_input $1 ec2)
    if [ $(abcli_list_in "$target" "all|docker|ec2|jetson|headless_rpi|mac|rpi" --delim "|") != True ]; then

        local function_name=${target}_seed
        if [[ $(type -t $function_name) == "function" ]]; then
            $function_name "${@:2}"
            return
        fi

        abcli_log_error "-abcli: seed: $target: target not found."
        return 1
    fi

    local options=$2
    local output="clipboard"
    local filename=""
    local to_key=$(abcli_option_int "$options" key 0)
    if [ "$to_key" == 1 ]; then
        local output="key"
    else
        local to_screen=$(abcli_option_int "$options" screen 0)
        if [ "$to_screen" == 1 ]; then
            local output="screen"
        else
            local filename=$(abcli_option "$options" filename)
        fi
    fi

    local options=$3
    local do_log=$(abcli_option_int "$options" log 1)
    local cookie_name=""
    if [ "$target" == "ec2" ]; then
        local cookie_name="worker"
    fi
    local cookie_name=$(abcli_option "$options" cookie $cookie_name)

    if [ "$target" == "all" ]; then
        local target_
        for target_ in ec2 jetson headless_rpi mac rpi; do
            abcli_seed $target_ ${@:2}
        done
        return
    fi

    if [ "$output" == "key" ]; then
        if [[ "$abcli_is_jetson" == true ]]; then
            local seed_path="/media/abcli/SEED"
        else
            local seed_path="/Volumes/seed"
        fi

        if [ ! -d "$seed_path" ]; then
            abcli_log_error "-abcli: seed: usb key not found."
            return
        fi

        mkdir -p $seed_path/abcli/
    fi

    if [ "$do_log" == 1 ]; then
        abcli_log "seed: $abcli_fullname -$target-> $output 🌱"
    fi

    local sudo_prefix="sudo "
    local delim="\n"
    local delim_section="\n\n"
    seed="#! /bin/bash$delim"
    if [ "$output" == "clipboard" ]; then
        local delim="; "
        local delim_section="; "
        seed=""
    fi

    seed="${seed}echo \"$abcli_fullname seed for $target\"$delim_section"

    if [ "$target" == docker ]; then
        seed="${seed}source /root/git/awesome-bash-cli/bash/abcli.sh$delim"
    else
        seed="${seed}mkdir -p \$HOME/.kaggle$delim"
        seed="$seed$(abcli_seed add_file .kaggle/kaggle.json output=$output)$delim"
        seed="${seed}chmod 600 \$HOME/.kaggle/kaggle.json$delim_section"

        seed="$seed${sudo_prefix}rm -rf ~/.aws$delim"
        seed="$seed${sudo_prefix}mkdir ~/.aws$delim_section"
        seed="$seed$(abcli_seed add_file .aws/config output=$output)$delim"
        seed="$seed$(abcli_seed add_file .aws/credentials output=$output)$delim_section"

        seed="${seed}${sudo_prefix}mkdir -p ~/.ssh$delim_section"
        seed="$seed"'eval "$(ssh-agent -s)"'"$delim_section"
        seed="$seed$(abcli_seed add_file .ssh/$abcli_git_ssh_key_name output=$output)$delim"
        seed="${seed}chmod 600 ~/.ssh/$abcli_git_ssh_key_name$delim"
        seed="${seed}ssh-add -k ~/.ssh/$abcli_git_ssh_key_name$delim_section"

        if [ "$target" == "headless_rpi" ] || [ "$target" == "rpi" ]; then
            seed="${seed}ssh-keyscan github.com | sudo tee -a ~/.ssh/known_hosts$delim_section"
        fi

        seed="${seed}"'ssh -T git@github.com'"$delim_section"

        if [ "$target" == "headless_rpi" ] || [ "$target" == "rpi" ]; then
            # https://serverfault.com/a/1093530
            # https://packages.ubuntu.com/bionic/all/ca-certificates/download
            certificate_name="ca-certificates_20211016ubuntu0.18.04.1_all"
            seed="${seed}wget --no-check-certificate http://security.ubuntu.com/ubuntu/pool/main/c/ca-certificates/$certificate_name.deb$delim"
            seed="$seed${sudo_prefix}sudo dpkg -i $certificate_name.deb$delim_section"

            seed="$seed${sudo_prefix}apt-get update --allow-releaseinfo-change$delim"
            seed="$seed${sudo_prefix}apt-get install -y ca-certificates libgnutls30$delim"
            seed="$seed${sudo_prefix}apt-get --yes --force-yes install git$delim_section"
        fi

        seed="${seed}cd; mkdir -p git; cd git$delim"
        seed="${seed}git clone git@github.com:kamangir/awesome-bash-cli.git$delim"
        seed="${seed}cd awesome-bash-cli${delim}"
        seed="${seed}git checkout $abcli_git_branch; git pull$delim_section"

        pushd $abcli_path_bash/bootstrap/config >/dev/null
        local filename
        for filename in *.sh *.json *.pem; do
            seed="$seed$(abcli_seed add_file git/awesome-bash-cli/bash/bootstrap/config/$filename output=$output)$delim_section"
        done
        popd >/dev/null

        if [ "$target" == "headless_rpi" ]; then
            seed="${seed}touch ~/git/awesome-bash-cli/bash/bootstrap/cookie/headless$delim_section"
        fi

        if [ "$target" == "rpi" ]; then
            seed="${seed}python3 -m pip install --upgrade pip$delim"
            seed="${seed}pip3 install -e .$delim"
            seed="${seed}sudo python3 -m pip install --upgrade pip$delim"
            seed="${seed}sudo pip3 install -e .$delim_section"
        elif [ "$target" == "headless_rpi" ]; then
            seed="${seed}sudo apt-get --yes --force-yes install python3-pip$delim"
            seed="${seed}pip3 install -e .$delim"
            seed="${seed}sudo pip3 install -e .$delim_section"
        else
            seed="${seed}pip3 install -e .$delim_section"
        fi

        seed="${seed}source ./bash/abcli.sh$delim_section"

        if [ "$target" == "ec2" ]; then
            seed="${seed}source ~/.bash_profile$delim_section"
        elif [ "$target" == "rpi" ]; then
            seed="${seed}source ~/.bashrc$delim_section"
        fi

        if [ ! -z "$cookie_name" ]; then
            seed="${seed}abcli cookie copy $cookie_name$delim"
            seed="${seed}abcli init$delim_section"
        fi
    fi

    if [ "$output" == "clipboard" ]; then
        if [ "$abcli_is_mac" == true ]; then
            echo $seed | pbcopy
        elif [ "$abcli_is_ubuntu" == true ]; then
            echo $seed | xclip -sel clip
        fi
        if [ "$do_log" == 1 ]; then
            abcli_log "📋 paste the seed 🌱 in the $target terminal."
        fi
    elif [ "$output" == "key" ] || [ "$output" == "file" ]; then
        if [ "$output" == "key" ]; then
            local filename="$seed_path/abcli/$target"
        else
            local filename=$(abcli_option "$options" filename $abcli_object_path/seed)
        fi

        echo -en $seed >$filename.sh
        chmod +x $filename.sh

        echo "{\"version\":\"$abcli_version\"}" >$filename.json

        if [ "$do_log" == 1 ]; then
            abcli_log "seed 🌱 -> $filename."
        fi
    elif [ "$output" == "screen" ]; then
        printf "$GREEN$seed$NC\n"
    else
        if [ "$do_log" == 1 ]; then
            abcli_log_error "-abcli: seed: $output: output not found."
        fi
    fi
}
