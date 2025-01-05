from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions


def help_perform_action(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "action=<action-name>,plugin=<plugin-name>"

    return show_usage(
        [
            "@perform_action",
            f"[{options}]",
            "<args>",
        ],
        "perform the action.",
        mono=mono,
    )
