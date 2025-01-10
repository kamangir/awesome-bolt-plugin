from typing import List

from blue_options.terminal import show_usage, xtra


def help_publish(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra(
        "as=<public-object-name>,~download,prefix=<prefix>,suffix=<.png>",
        mono=mono,
    )

    return show_usage(
        [
            "@publish",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "publish <object-name>.",
        mono=mono,
    )


def help_publish_tar(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("as=<public-object-name>,~download,", mono=mono),
            "tar",
        ]
    )

    return show_usage(
        [
            "@publish",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "publish <object-name>.tar.gz.",
        mono=mono,
    )


help_functions = {
    "": help_publish,
    "tar": help_publish_tar,
}
