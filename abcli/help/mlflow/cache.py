from typing import List

from blue_options.terminal import show_usage


def help_read(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@mlflow",
            "cache",
            "read",
            "<keyword>",
        ],
        "read mlflow.cache[<keyword>].",
        mono=mono,
    )


def help_write(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@mlflow",
            "cache",
            "write",
            "<keyword>",
            "<value>",
        ],
        "write mlflow.cache[<keyword>]=value.",
        mono=mono,
    )


help_functions = {
    "read": help_read,
    "write": help_write,
}
