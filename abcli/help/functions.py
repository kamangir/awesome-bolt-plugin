from typing import List

from blue_options.terminal import show_usage, xtra

from abcli.help.git import help_functions as help_git
from abcli.help.log import help_functions as help_log
from abcli.help.pytest import help_pytest


help_functions = {
    "git": help_git,
    "log": help_log,
    "pytest": help_pytest,
}
