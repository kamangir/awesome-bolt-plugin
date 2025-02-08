from typing import List

from blue_options.terminal import show_usage, xtra


def help_clone(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~content,cp,~download,", mono=mono),
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
