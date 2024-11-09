from typing import List

from blue_options.terminal import show_usage


def help_(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "backup",
        ],
        "backup env -> $abcli_path_env_backup.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "backup",
            "list",
        ],
        "list $abcli_path_env_backup.",
        mono=mono,
    )


help_functions = {
    "": help_,
    "list": help_list,
}
