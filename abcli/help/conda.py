from typing import List

from blue_options.terminal import show_usage, xtra


def help_create(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("clone=<auto|base>,~install_plugin,", mono=mono),
            "name=<environment-name>",
            xtra(",repo=<repo-name>,~recreate", mono=mono),
        ]
    )

    return show_usage(
        [
            "@conda",
            "create",
            f"[{options}]",
        ],
        "create conda environment.",
        mono=mono,
    )


def help_exists(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "name=<environment-name>"

    return show_usage(
        [
            "@conda",
            "exists",
            f"[{options}]",
        ],
        "does conda environment exist?",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@conda",
            "list",
            f"[{options}]",
        ],
        "show list of conda environments.",
        mono=mono,
    )


def help_rm(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "name=<environment-name>",
        ]
    )

    return show_usage(
        [
            "@conda",
            "rm",
            f"[{options}]",
        ],
        "rm conda environment.",
        mono=mono,
    )


help_functions = {
    "create": help_create,
    "exists": help_exists,
    "list": help_list,
    "rm": help_rm,
}
