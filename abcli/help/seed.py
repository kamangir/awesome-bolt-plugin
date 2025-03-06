from typing import List

from blue_options.terminal import show_usage, xtra


def help_(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "clipboard|filename=<filename>|key|screen,env=<env-name>,eval,plugin=<plugin-name>,~log"

    return show_usage(
        [
            "@seed",
            "<target>",
            f"[{options}]",
            "[cat,dryrun]",
            "<command-line>",
        ],
        "generate and output a seed 🌱 .",
        mono=mono,
    )


def help_eject(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@seed",
            "eject",
        ],
        "eject seed 🌱 .",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@seed",
            "list",
        ],
        "list seed 🌱  targets.",
        mono=mono,
    )


help_functions = {
    "": help_,
    "eject": help_eject,
    "list": help_list,
}
