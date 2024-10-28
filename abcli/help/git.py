import os
from typing import List

from blue_options.terminal import show_usage, xtra


def help(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "<repo_name>",
            "<command-line>",
        ],
        "run '@git <command-line>' in <repo_name>.",
        mono=mono,
    )


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions"

    return show_usage(
        [
            "@git",
            "browse",
            "[ . | - | <repo-name> ]",
            f"[{options}]",
        ],
        "browse <repo-name>.",
        mono=mono,
    )


def help_checkout(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "rebuild"

    return show_usage(
        [
            "@git",
            "checkout",
            "<branch-name> | <path/filename>",
            f"[{options}]",
            "[<args>]",
        ],
        "git checkout <args>.",
        mono=mono,
    )


def help_clone(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("cd,~from_template,if_cloned,init,", mono=mono),
            "install",
            xtra(",object,pull,source=<username/repo_name>", mono=mono),
        ]
    )

    return show_usage(
        [
            "@git",
            "clone",
            "<repo-name>",
            f"[{options}]",
        ],
        "clone <repo-name>.",
        mono=mono,
    )


def help_create_branch(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~increment_version,~push,~timestamp", mono=mono)

    return show_usage(
        [
            "@git",
            "create_branch",
            "<branch-name>",
            f"[{options}]",
        ],
        "create <branch-name> in the repo.",
        mono=mono,
    )


def help_create_pull_request(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "create_pull_request",
        ],
        "create a pull request in the repo.",
        mono=mono,
    )


def help_get_branch(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "get_branch",
        ],
        "get git branch name.",
        mono=mono,
    )


def help_get_repo_name(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "get_repo_name",
        ],
        "get repo name.",
        mono=mono,
    )


def help_increment_version(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "diff"

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@git",
            "++ | increment | increment_version",
            f"[{options}]",
        ]
        + args,
        "increment repo version.",
        mono=mono,
    )


def help_pull(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~all,", mono=mono),
            "init",
        ]
    )

    return show_usage(
        [
            "@git",
            "pull",
            f"[{options}]",
        ],
        "pull.",
        mono=mono,
    )


def help_push(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~action,", mono=mono),
            "browse",
            xtra(",~create_pull_request,", mono=mono),
            "first",
            xtra(",~increment_version,~status", mono=mono),
        ]
    )

    build_options = "build,{}".format(os.getenv("abcli_pypi_build_options"))

    return show_usage(
        [
            "@git",
            "push",
            "<message>",
            f"[{options}]",
            f"[{build_options}]",
        ],
        "push to the repo.",
        mono=mono,
    )


def help_recreate_ssh(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "recreate_ssh",
        ],
        "recreate github ssh key.",
        mono=mono,
    )


def help_reset(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "reset",
        ],
        "reset to the latest commit of the current branch.",
        mono=mono,
    )


def help_review(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "review",
        ],
        "review the repo.",
        mono=mono,
    )


def help_status(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "~all"

    return show_usage(
        [
            "@git",
            "status",
            f"[{options}]",
        ],
        "show git status.",
        mono=mono,
    )


def help_sync_fork(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@git",
            "sync_fork",
            "<branch-name>",
        ],
        "sync fork w/ upstream.",
        mono=mono,
    )


help_functions = {
    "": help,
    "browse": help_browse,
    "checkout": help_checkout,
    "clone": help_clone,
    "create_branch": help_create_branch,
    "create_pull_request": help_create_pull_request,
    "get_branch": help_get_branch,
    "get_repo_name": help_get_repo_name,
    "increment_version": help_increment_version,
    "pull": help_pull,
    "push": help_push,
    "recreate_ssh": help_recreate_ssh,
    "reset": help_reset,
    "review": help_review,
    "status": help_status,
    "sync_fork": help_sync_fork,
}
