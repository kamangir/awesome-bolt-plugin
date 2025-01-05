from typing import List

from blue_options.terminal import show_usage, xtra


def help_trail(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@trail",
            "<filename>",
        ],
        "<filename> -> papertrail.",
        mono=mono,
    )


def help_trail_stop(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@trail",
            "stop",
        ],
        "stop papertrail.",
        mono=mono,
    )


help_functions = {
    "": help_trail,
    "stop": help_trail_stop,
}
