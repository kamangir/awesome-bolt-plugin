from typing import List

from blue_options.terminal import show_usage, xtra


def help_(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@terraform",
        ],
        "terraform this machine.",
        mono=mono,
    )


def help_cat(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@terraform",
            "cat",
        ],
        "cat terraform files.",
        mono=mono,
    )


def help_disable(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@terraform",
            "disable",
        ],
        "disable terraform.",
        mono=mono,
    )


def help_enable(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@terraform",
            "enable",
        ],
        "enable terraform.",
        mono=mono,
    )


help_functions = {
    "": help_,
    "cat": help_cat,
    "disable": help_disable,
    "enable": help_enable,
}
