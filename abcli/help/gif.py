from typing import List

from blue_options.terminal import show_usage, xtra


def help_gif(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~upload", mono=mono)

    args = [
        "[--frame_duration <150>]",
        "[--output_filename <object-name>.gif]",
        "[--scale <1>]",
        "[--suffix <.png>]",
    ]

    return show_usage(
        [
            "@gif",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "generate <object-name>.gif.",
        mono=mono,
    )
