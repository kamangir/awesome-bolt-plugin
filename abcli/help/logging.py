from typing import List

from blue_options.terminal import show_usage, xtra


def help_cat(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@cat",
            "<filename>",
        ],
        "cat <filename>.",
        mono=mono,
    )


def help_log(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@log",
            "<message>",
        ],
        "log message.",
        mono=mono,
    )


def help_log_list(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        '[--before "list of"]',
        '[--after "items(s)"]',
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "abcli_log_list",
            "<this,that>",
        ]
        + args,
        "log list.",
        mono=mono,
    )


def help_log_verbose(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "on | off"

    return show_usage(
        [
            "@log",
            "verbose",
            f"[{options}]",
        ],
        "verbose logging on/off.",
        mono=mono,
    )


help_functions = {
    "": help_log,
    "list": help_log_list,
    "verbose": help_log_verbose,
}
