from typing import List, Dict, Callable, Union

from blue_options.terminal import show_usage, xtra


def help_(
    tokens: List[str],
    mono: bool,
    plugin_name: str = "abcli",
) -> str:
    options = xtra(
        "what=all|<test-name>,dryrun",
        mono=mono,
    )

    test_options = xtra(
        "dryrun",
        mono=mono,
    )

    callable = f"{plugin_name} test"

    if plugin_name == "abcli":
        options = f"{options},plugin=<plugin-name>"
        callable = "@test"

    return show_usage(
        callable.split(" ")
        + [
            f"[{options}]",
            f"[{test_options}]",
        ],
        f"test {plugin_name}.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
    plugin_name: str = "abcli",
) -> str:
    options = "list"

    callable = f"{plugin_name} test"

    if plugin_name == "abcli":
        options = f"{options},plugin=<plugin-name>"
        callable = "@test"

    return show_usage(
        callable.split(" ")
        + [
            f"{options}",
        ],
        f"list {plugin_name} tests.",
        mono=mono,
    )


def help_functions(
    plugin_name: str = "abcli",
) -> Union[Callable, Dict[str, Union[Callable, Dict]]]:
    return {
        "": lambda tokens, mono: help_(
            tokens,
            mono=mono,
            plugin_name=plugin_name,
        ),
        "list": lambda tokens, mono: help_list(
            tokens,
            mono=mono,
            plugin_name=plugin_name,
        ),
    }
