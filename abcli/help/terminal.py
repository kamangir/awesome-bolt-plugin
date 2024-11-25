from typing import List

from blue_options.terminal import show_usage


def help_badge(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@badge",
            'clear | "🪄"',
        ],
        "update badge.",
        mono=mono,
    )
