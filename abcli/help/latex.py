from typing import List

from blue_options.terminal import show_usage, xtra


def build_options(mono: bool):
    return "".join(
        [
            "bib=<name>",
            xtra(",dryrun,install,~ps,~pdf", mono=mono),
        ]
    )


def help_build(
    tokens: List[str],
    mono: bool,
) -> str:
    options = build_options(mono)

    return show_usage(
        [
            "@latex",
            "build",
            f"[{options}]",
            "<path/filename.tex>",
        ],
        "build <path/filename.tex>.",
        mono=mono,
    )


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@latex",
            "install",
        ],
        "install latex.",
        mono=mono,
    )


help_functions = {
    "build": help_build,
    "install": help_install,
}
