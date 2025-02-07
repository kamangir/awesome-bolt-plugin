from typing import List

from blue_options.terminal import show_usage, xtra


def help_cat(
    tokens: List[str],
    mono: bool,
) -> str:
    return "\n".join(
        [
            show_usage(
                [
                    "@env",
                    "dot",
                    "cat",
                    "[ | <env-name> | config | sample ]",
                ],
                "cat env.",
                mono=mono,
            ),
            show_usage(
                [
                    "@env",
                    "dot",
                    "cat",
                    "jetson_nano | rpi",
                    "<machine-name>",
                ],
                "cat .env from machine.",
                mono=mono,
            ),
        ]
    )


def help_cp(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "dot",
            "cp | copy",
            "<env-name>",
            "local | jetson_nano | rpi",
            "[<machine-name>]",
        ],
        "cp <env-name> to machine.",
        mono=mono,
    )


def help_edit(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "dot",
            "edit",
            "jetson_nano | rpi",
            "<machine-name>",
        ],
        "edit .env on machine.",
        mono=mono,
    )


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "dot",
            "get",
            "<variable>",
        ],
        "<variable>.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "dot",
            "list",
        ],
        "list env repo.",
        mono=mono,
    )


def help_load(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "caller,filename=<.env>,plugin=<plugin-name>,ssm,suffix=/tests,verbose"

    return show_usage(
        [
            "@env",
            "dot",
            "load",
            f"[{options}]",
        ],
        "load .env.",
        mono=mono,
    )


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@env",
            "dot",
            "set",
            "<variable>",
            "<value>",
        ],
        "<variable> = <value>.",
        mono=mono,
    )


help_functions = {
    "cat": help_cat,
    "cp": help_cp,
    "edit": help_edit,
    "get": help_get,
    "list": help_list,
    "load": help_load,
    "set": help_set,
}
