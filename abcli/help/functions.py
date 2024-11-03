from typing import List

from blue_options.terminal import show_usage, xtra

from abcli.help.cp import help_cp
from abcli.help.download import help_download
from abcli.help.gif import help_gif
from abcli.help.git import help_functions as help_git
from abcli.help.gpu import help_functions as help_gpu
from abcli.help.init import help_init
from abcli.help.log import help_functions as help_log
from abcli.help.metadata import help_functions as help_metadata
from abcli.help.mlflow import help_functions as help_mlflow
from abcli.help.notebooks import help_functions as help_notebooks
from abcli.help.pytest import help_pytest


help_functions = {
    "cp": help_cp,
    "download": help_download,
    "gif": help_gif,
    "git": help_git,
    "gpu": help_gpu,
    "init": help_init,
    "log": help_log,
    "metadata": help_metadata,
    "mlflow": help_mlflow,
    "notebooks": help_notebooks,
    "pytest": help_pytest,
}
