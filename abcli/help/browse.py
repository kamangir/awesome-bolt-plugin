from typing import List

from blue_options.terminal import show_usage


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions|repo"

    return show_usage(
        [
            "@browse",
            "<url>",
            "[<description>]",
        ],
        "browse <url>.",
        mono=mono,
    )
