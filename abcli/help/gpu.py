from typing import List

from blue_options.terminal import show_usage, xtra


def help_gpu_status_get(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "~from_cache"

    return show_usage(
        [
            "@gpu",
            "status",
            "get",
            f"[{options}]",
        ],
        "get gpu status.",
        mono=mono,
    )


def help_gpu_status_show(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@gpu",
            "status",
            "show",
        ],
        "show gpu status.",
        mono=mono,
    )


def help_gpu_validate(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@gpu",
            "validate",
        ],
        "validate gpu.",
        mono=mono,
    )


help_functions = {
    "status": {
        "get": help_gpu_status_get,
        "show": help_gpu_status_show,
    },
    "validate": help_gpu_validate,
}
