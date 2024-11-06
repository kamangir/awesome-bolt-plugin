from typing import List

from blue_options.terminal import show_usage, xtra


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "filename=<filename>",
            xtra(",mlflow,no_mlflow,~open,", mono=mono),
            "solid",
            xtra(",~warn_if_exists", mono=mono),
        ]
    )

    return show_usage(
        [
            "@upload",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "upload <object-name>.",
        mono=mono,
    )
