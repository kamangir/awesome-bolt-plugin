from typing import List

from blue_options.terminal import show_usage, xtra

from abcli.help.git import help_functions as help_git
from abcli.help.log import help_functions as help_log
from abcli.help.notebooks import help_functions as help_notebooks
from abcli.help.pytest import help_pytest


help_functions = {
    "git": help_git,
    "log": help_log,
    "notebooks": help_notebooks,
    "pytest": help_pytest,
}
