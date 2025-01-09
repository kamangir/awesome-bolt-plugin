from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions
from abcli.help.latex import build_options as latex_build_options

from abadpour import ALIAS


def help_build(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra(
        "dryrun,~publish,~rm,what=<cv+cv-full>",
        mono=mono,
    )

    return show_usage(
        [
            "CV",
            "build",
            f"[{options}]",
            f"[{latex_build_options(mono=mono)}]",
        ],
        "build CV.",
        mono=mono,
    )


def help_clean(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "CV",
            "clean",
        ],
        "clean CV.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "build": help_build,
        "clean": help_clean,
    }
)
