from typing import List

from blue_options.terminal import show_usage, xtra

default_list_of_extensions = [
    "png",
    "geojson",
]


def help_publish(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("download,", mono=mono),
            "extension={},push".format("+".join(default_list_of_extensions)),
        ]
    )

    return show_usage(
        [
            "@assets",
            "publish",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "<object-name -> assets.",
        mono=mono,
    )


help_functions = {
    "publish": help_publish,
}
