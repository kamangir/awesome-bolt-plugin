from typing import List

from blue_options.terminal import show_usage, xtra


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dashboard"

    return show_usage(
        [
            "@sagemaker",
            "browse",
            f"[{options}]",
        ],
        "browse sagemaker.",
        mono=mono,
    )


help_functions = {
    "browse": help_browse,
}
