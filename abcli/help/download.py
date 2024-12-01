from typing import List

from blue_options.terminal import show_usage, xtra


def help_download(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "filename=<filename>"

    open_options = "open,QGIS"

    return show_usage(
        [
            "@download",
            f"[{options}]",
            "[.|<object-name>]",
            f"[{open_options}]",
        ],
        "download object.",
        mono=mono,
    )
