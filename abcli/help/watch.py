from typing import List

from blue_options.terminal import show_usage


def help_watch(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "~clear,dryrun,seconds=<seconds>"

    return show_usage(
        [
            "@watch",
            f"[{options}]",
            "<command-line>",
        ],
        "watch <command-line>.",
        mono=mono,
    )
