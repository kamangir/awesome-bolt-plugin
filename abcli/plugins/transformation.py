from typing import Dict
from tqdm import tqdm
import glob
import os

from blueness import module
from blue_objects import file
from blue_objects.env import abcli_path_git

from abcli import NAME
from abcli.logger import logger

NAME = module.name(__file__, NAME)


def transform(
    repo_name: str,
    plugin_name: str,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.transform: {} @ {}".format(
            NAME,
            repo_name,
            plugin_name,
        )
    )

    repo_path = os.path.join(abcli_path_git, repo_name)
    logger.info(f"repo_path: {repo_path}")

    alias_name: str = ""
    if repo_name.startswith("blue-"):
        alias_name = "@{}".format(repo_name.split("blue-", 1)[1])
        logger.info(f"alias: {alias_name}")

    transformation: Dict[str, str] = {
        "blue_plugin": plugin_name,
        "blue-plugin": repo_name,
        "BLUE_PLUGIN": plugin_name.upper(),
    }
    if alias_name:
        transformation["@plugin"] = alias_name
    logger.info(f"{len(transformation)} transformation(s)")
    for index, (this, that) in enumerate(transformation.items()):
        logger.info(f"#{index: 2d} - {this} -> {that}")

    list_of_extensions = "env,py,sh,yml".split(",")

    for root, _, list_of_filenames in tqdm(os.walk(repo_path)):
        for filename in list_of_filenames:
            if any(
                filename.endswith(f".{extension}") for extension in list_of_extensions
            ):
                full_filename = os.path.join(root, filename)

                success, content = file.load_text(
                    full_filename,
                    log=verbose,
                )
                if not success:
                    return False

                for this, that in transformation.items():
                    content = [line.replace(this, that) for line in content]

                success = file.save_text(
                    full_filename,
                    content,
                    log=log,
                )
                if not success:
                    return False

    return True
