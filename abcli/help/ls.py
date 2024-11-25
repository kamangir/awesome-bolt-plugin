from typing import List

from blue_options.terminal import show_usage


def help_ls(
    tokens: List[str],
    mono: bool,
) -> str:
    return "\n".join(
        [
            show_usage(
                [
                    "@ls",
                    "cloud | local",
                    "<object-name>",
                ],
                "ls <object-name>",
                mono=mono,
            ),
            show_usage(
                [
                    "@ls",
                    "<path>",
                ],
                "ls <path>.",
                mono=mono,
            ),
        ]
    )
