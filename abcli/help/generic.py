from typing import List, Dict, Callable, Union

from abcli.help.pypi import help_functions as help_pypi
from abcli.help.pylint import help_pylint
from abcli.help.pytest import help_pytest
from abcli.help.test import help_functions as help_test


def help_functions(
    plugin_name: str = "abcli",
) -> Union[Callable, Dict[str, Union[Callable, Dict]]]:
    return {
        "pypi": help_pypi(plugin_name=plugin_name),
        "pylint": lambda tokens, mono: help_pylint(
            tokens,
            mono=mono,
            plugin_name=plugin_name,
        ),
        "pytest": lambda tokens, mono: help_pytest(
            tokens,
            mono=mono,
            plugin_name=plugin_name,
        ),
        "test": help_test(plugin_name=plugin_name),
    }
