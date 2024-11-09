from typing import List

from blue_options.terminal import show_usage


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@browse",
            "<url>",
            "[<description>]",
        ],
        "browse <url>.",
        mono=mono,
    )
