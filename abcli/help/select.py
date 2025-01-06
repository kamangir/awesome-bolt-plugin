from typing import List

from blue_options.terminal import show_usage, xtra


def help_select(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("open,type=<type>,~trail", mono=mono)

    return show_usage(
        [
            "@select",
            "[-|<object-name>]",
            f"[{options}]",
        ],
        "select <object-name>.",
        mono=mono,
    )
