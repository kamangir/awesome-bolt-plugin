from typing import List, Dict, Callable, Union

from blue_options.terminal import show_usage, xtra

build_options = "browse,install,~rm_dist,~upload"


def help_browse(
    tokens: List[str],
    mono: bool,
    plugin_name: str = "abcli",
) -> str:
    options = "token"

    callable = f"{plugin_name} pypi"

    if plugin_name == "abcli":
        options = f"plugin=<plugin-name>,{options}"
        callable = "@pypi"

    return show_usage(
        callable.split(" ")
        + [
            "browse",
            f"[{options}]",
        ],
        f"browse pypi/{plugin_name}.",
        mono=mono,
    )


def help_build(
    tokens: List[str],
    mono: bool,
    plugin_name: str = "abcli",
) -> str:
    options = xtra(build_options, mono=mono)

    callable = f"{plugin_name} pypi"

    if plugin_name == "abcli":
        options = f"{options},plugin=<plugin-name>"
        callable = "@pypi"

    return show_usage(
        callable.split(" ")
        + [
            "build",
            f"[{options}]",
        ],
        f"build pypi/{plugin_name}.",
        mono=mono,
    )


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@pypi",
            "install",
        ],
        "install pypi.",
        mono=mono,
    )


def help_functions(
    plugin_name: str = "abcli",
) -> Union[Callable, Dict[str, Union[Callable, Dict]]]:
    return {
        "browse": lambda tokens, mono: help_browse(
            tokens,
            mono=mono,
            plugin_name=plugin_name,
        ),
        "build": lambda tokens, mono: help_build(
            tokens,
            mono=mono,
            plugin_name=plugin_name,
        ),
        "install": help_install,
    }
