from typing import List

from blue_options.terminal import show_usage, xtra


def help_pause(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra(
        "dryrun,message=<dash-separated-message>",
        mono=mono,
    )

    return show_usage(
        [
            "@pause",
            f"[{options}]",
        ],
        "show <message> and pause for key press.",
        mono=mono,
    )
