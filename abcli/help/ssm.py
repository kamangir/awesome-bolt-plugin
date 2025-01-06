from typing import List

from blue_options.terminal import show_usage


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    return "\n".join(
        [
            show_usage(
                [
                    "@ssm",
                    "get",
                    "<secret-name>",
                ],
                "get <secret-name>.",
                mono=mono,
            ),
            show_usage(
                [
                    "@ssm",
                    "get",
                    "path=<path>",
                ],
                "get <path>/sample.env secrets.",
                mono=mono,
            ),
        ]
    )


def help_put(
    tokens: List[str],
    mono: bool,
) -> str:
    return "\n".join(
        [
            show_usage(
                [
                    "@ssm",
                    "put",
                    "<secret-name>",
                    "<secret-value>",
                ]
                + ["[--description <description>]"],
                "put <secret-name> = <secret-value>.",
                mono=mono,
            ),
            show_usage(
                [
                    "@ssm",
                    "put",
                    "plugin=<plugin-name>",
                ],
                "put <plugin-name> secrets.",
                mono=mono,
            ),
            show_usage(
                [
                    "@ssm",
                    "put",
                    "repo=<repo-name>",
                ],
                "put <repo-name> secrets.",
                mono=mono,
            ),
        ]
    )


def help_rm(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@ssm",
            "rm",
            "<secret-name>",
        ],
        "rm <secret-name>.",
        mono=mono,
    )


help_functions = {
    "get": help_get,
    "put": help_put,
    "rm": help_rm,
}
