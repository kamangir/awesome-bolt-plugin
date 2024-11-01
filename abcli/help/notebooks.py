from typing import List

from blue_options.terminal import show_usage, xtra


def help_build(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@notebooks",
            "build",
            "[<notebook-name>]",
        ],
        "build <notebook-name>.",
        mono=mono,
    )


def help_code(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@notebooks",
            "code",
            "[<notebook-name>]",
        ],
        "code <notebook-name>.",
        mono=mono,
    )


def help_connect(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "ip=<1-2-3-4>",
            xtra(",setup", mono=mono),
        ]
    )

    return show_usage(
        [
            "@notebooks",
            "connect",
            f"[{options}]",
        ],
        "connect to jupyter notebook on ec2:<1-2-3-4>.",
        mono=mono,
    )


def help_create(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@notebooks",
            "create | touch",
            "<notebook-name> | <path>/<notebook-name> | notebook",
        ],
        "create <notebook-name>.",
        mono=mono,
    )


def help_host(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("setup", mono=mono)

    return show_usage(
        [
            "@notebooks",
            "host",
            f"[{options}]",
        ],
        "host jupyter notebook on ec2.",
        mono=mono,
    )


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@notebooks",
            "open",
            "[<notebook-name> | notebook]",
            "[<args>]",
        ],
        "open <notebook-name>.",
        mono=mono,
    )


help_functions = {
    "build": help_build,
    "code": help_code,
    "connect": help_connect,
    "create": help_create,
    "host": help_host,
    "open": help_open,
}
