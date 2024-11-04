from typing import List

from blue_options.terminal import show_usage


def help_sleep(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "seconds=<seconds>"

    return show_usage(
        [
            "@sleep",
            f"[{options}]",
        ],
        "sleep.",
        mono=mono,
    )
