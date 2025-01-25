from typing import List

from blue_options.terminal import show_usage, xtra


def help_clear(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "~dryrun"

    return show_usage(
        [
            "@storage",
            "clear",
            f"[{options}]",
        ],
        "clear storage.",
        mono=mono,
    )


def help_download_file(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@storage",
            "download_file",
            "<object-name>",
            "[filename]",
        ],
        "download filename -> <object-name>.",
        mono=mono,
    )


def help_exists(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@storage",
            "exists",
            "<object-name>",
        ],
        "True/False.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@storage",
            "list",
            "<prefix>",
            "[<args>]",
        ],
        "list prefix in storage.",
        mono=mono,
    )


def help_rm(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "~dryrun"

    return show_usage(
        [
            "@storage",
            "rm",
            f"[{options}]",
            "<object-name>",
        ],
        "rm <object-name>.",
        mono=mono,
    )


def help_status(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "count=<10>,depth=<2>"

    return show_usage(
        [
            "@storage",
            "status",
            f"[{options}]",
        ],
        "show storage status.",
        mono=mono,
    )


help_functions = {
    "clear": help_clear,
    "download_file": help_download_file,
    "exists": help_exists,
    "list": help_list,
    "rm": help_rm,
    "status": help_status,
}
