from typing import List

from blue_options.terminal import show_usage, xtra


def help_cp(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("cp,~download,", mono=mono),
            "~relate",
            xtra(",~tags,", mono=mono),
            "upload",
        ]
    )

    return show_usage(
        [
            "@cp",
            f"[{options}]",
            "[..|<object-1>]",
            "[.|<object-2>]",
        ],
        "copy <object-1> -> <object-2>.",
        mono=mono,
    )
