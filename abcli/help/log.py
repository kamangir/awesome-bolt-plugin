from typing import List

from blue_options.terminal import show_usage, xtra


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
    "verbose": help_log_verbose,
}
