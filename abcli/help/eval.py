from typing import List

from blue_options.terminal import show_usage, xtra


def options(mono: bool):
    return xtra(
        "dryrun,~log,path=<path>",
        mono=mono,
    )


def help_eval(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@eval",
            f"[{options(mono=mono)}]",
            "<command-line>",
        ],
        "eval <command-line>.",
        mono=mono,
    )
