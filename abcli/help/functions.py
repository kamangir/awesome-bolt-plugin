from abcli.help.generic import help_functions as generic_help_functions

from abcli.help.aws_batch import help_functions as help_aws_batch
from abcli.help.browse import help_browse
from abcli.help.cp import help_cp
from abcli.help.docker import help_functions as help_docker
from abcli.help.download import help_download
from abcli.help.env import help_functions as help_env
from abcli.help.eval import help_eval
from abcli.help.gif import help_gif
from abcli.help.git import help_functions as help_git
from abcli.help.gpu import help_functions as help_gpu
from abcli.help.init import help_init
from abcli.help.latex import help_functions as help_latex
from abcli.help.logging import help_cat
from abcli.help.logging import help_functions as help_log
from abcli.help.list import help_functions as help_list
from abcli.help.ls import help_ls
from abcli.help.metadata import help_functions as help_metadata
from abcli.help.mlflow import help_functions as help_mlflow
from abcli.help.notebooks import help_functions as help_notebooks
from abcli.help.plugins import help_functions as help_plugins
from abcli.help.open import help_open
from abcli.help.pause import help_pause
from abcli.help.repeat import help_repeat
from abcli.help.sagemaker import help_functions as help_sagemaker
from abcli.help.seed import help_functions as help_seed
from abcli.help.sleep import help_sleep
from abcli.help.source import (
    help_source_caller_suffix_path,
    help_source_path,
)
from abcli.help.terminal import help_badge
from abcli.help.terraform import help_functions as help_terraform
from abcli.help.upload import help_upload
from abcli.help.watch import help_watch

help_functions = generic_help_functions(plugin_name="abcli")


help_functions.update(
    {
        "aws_batch": help_aws_batch,
        "badge": help_badge,
        "browse": help_browse,
        "cat": help_cat,
        "cp": help_cp,
        "docker": help_docker,
        "download": help_download,
        "env": help_env,
        "eval": help_eval,
        "gif": help_gif,
        "git": help_git,
        "gpu": help_gpu,
        "init": help_init,
        "latex": help_latex,
        "log": help_log,
        "list": help_list,
        "ls": help_ls,
        "metadata": help_metadata,
        "mlflow": help_mlflow,
        "notebooks": help_notebooks,
        "open": help_open,
        "pause": help_pause,
        "plugins": help_plugins,
        "repeat": help_repeat,
        "sagemaker": help_sagemaker,
        "seed": help_seed,
        "sleep": help_sleep,
        "source_caller_suffix_path": help_source_caller_suffix_path,
        "source_path": help_source_path,
        "terraform": help_terraform,
        "upload": help_upload,
        "watch": help_watch,
    }
)
