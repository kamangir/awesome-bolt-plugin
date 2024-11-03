from typing import List

from blue_options.terminal import show_usage, xtra


def help_init(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "clear,~terraform"

    return show_usage(
        [
            "@init",
            "[<plugin-name> | all | clear] ",
            f"[{options}]",
        ],
        "init [<plugin-name>].",
        mono=mono,
    )
