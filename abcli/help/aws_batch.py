from typing import List

from abcli import env

from blue_options.terminal import show_usage, xtra


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    # ---
    options = "cat,id=<job-id>,log"

    usage_1 = show_usage(
        [
            "@batch",
            "browse",
            f"[{options}]",
        ],
        "browse <job-id>.",
        mono=mono,
    )

    # ---
    options = "queue=<queue-name>,status=<status>"

    usage_2 = show_usage(
        [
            "@batch",
            "browse",
            f"[{options}]",
        ],
        "browse <queue-name>.",
        {
            "status: {}".format(
                " | ".join(env.ABCLI_AWS_BATCH_JOB_STATUS_LIST.split(","))
            ): "",
        },
        mono=mono,
    )

    # ---
    options = "queue=list"

    usage_3 = show_usage(
        [
            "@batch",
            "browse",
            f"[{options}]",
        ],
        "browse list of queues.",
        mono=mono,
    )

    return "\n".join(
        [
            usage_1,
            usage_2,
            usage_3,
        ]
    )


def help_cat(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "-"

    return show_usage(
        [
            "@batch",
            "cat",
            f"[{options}]",
            "<job-id>",
        ],
        "cat <job-id>.",
        mono=mono,
    )


def help_eval(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "cat,dryrun,name=<job-name>"

    return show_usage(
        [
            "@batch",
            "eval",
            f"[{options}]",
            "<command-line>",
        ],
        "eval <command-line> in aws batch.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "~count",
            xtra(
                ",dryrun,prefix=<prefix>,status=<status>",
                mono=mono,
            ),
        ]
    )

    return show_usage(
        [
            "@batch",
            "list",
            f"[{options}]",
        ],
        "list aws batch jobs.",
        {
            "status: {}".format(
                " | ".join(env.ABCLI_AWS_BATCH_JOB_STATUS_LIST.split(","))
            ): "",
        },
        mono=mono,
    )


def help_submit(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "cat,dryrun,name=<job-name>"

    return show_usage(
        [
            "@batch",
            "source",
            f"[{options}]",
            "<script-name>",
            "[<args>]",
        ],
        "source <script-name> in aws batch.",
        mono=mono,
    )


help_functions = {
    "browse": help_browse,
    "cat": help_cat,
    "eval": help_eval,
    "list": help_list,
    "submit": help_submit,
}
