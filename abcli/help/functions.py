from abcli.help.aws_batch import help_functions as help_aws_batch
from abcli.help.cp import help_cp
from abcli.help.docker import help_functions as help_docker
from abcli.help.download import help_download
from abcli.help.eval import help_eval
from abcli.help.gif import help_gif
from abcli.help.git import help_functions as help_git
from abcli.help.gpu import help_functions as help_gpu
from abcli.help.init import help_init
from abcli.help.latex import help_functions as help_latex
from abcli.help.log import help_functions as help_log
from abcli.help.metadata import help_functions as help_metadata
from abcli.help.mlflow import help_functions as help_mlflow
from abcli.help.notebooks import help_functions as help_notebooks
from abcli.help.plugins import help_functions as help_plugins
from abcli.help.open import help_open
from abcli.help.pytest import help_pytest
from abcli.help.repeat import help_repeat
from abcli.help.sagemaker import help_functions as help_sagemaker
from abcli.help.sleep import help_sleep
from abcli.help.terraform import help_functions as help_terraform
from abcli.help.upload import help_upload
from abcli.help.watch import help_watch


help_functions = {
    "aws_batch": help_aws_batch,
    "cp": help_cp,
    "docker": help_docker,
    "download": help_download,
    "eval": help_eval,
    "gif": help_gif,
    "git": help_git,
    "gpu": help_gpu,
    "init": help_init,
    "latex": help_latex,
    "log": help_log,
    "metadata": help_metadata,
    "mlflow": help_mlflow,
    "notebooks": help_notebooks,
    "open": help_open,
    "plugins": help_plugins,
    "pytest": help_pytest,
    "repeat": help_repeat,
    "sagemaker": help_sagemaker,
    "sleep": help_sleep,
    "terraform": help_terraform,
    "upload": help_upload,
    "watch": help_watch,
}
