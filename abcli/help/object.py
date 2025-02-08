from typing import List

from blue_options.terminal import show_usage, xtra


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@object",
            "open",
            "[.|<object-name>]",
        ],
        "open object.",
        mono=mono,
    )


help_functions = {
    "open": help_open,
}
