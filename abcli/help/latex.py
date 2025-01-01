from typing import List

from blue_options.terminal import show_usage, xtra


def help_bibclean(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,install", mono=mono)

    return show_usage(
        [
            "@latex",
            "bibclean",
            f"[{options}]",
            "<path/filename.bib>",
        ],
        "bibclean <path/filename.bib>.",
        mono=mono,
    )


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
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@latex",
            "install",
            f"[{options}]",
        ],
        "install latex.",
        mono=mono,
    )


help_functions = {
    "bibclean": help_bibclean,
    "build": help_build,
    "install": help_install,
}
