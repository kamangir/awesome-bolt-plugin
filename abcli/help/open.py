from typing import List

from blue_options.terminal import show_usage, xtra


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("extension=<extension>,filename=<filename>,", mono=mono),
            "QGIS",
        ]
    )

    return show_usage(
        [
            "@open",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "open <object-name>.",
        mono=mono,
    )
