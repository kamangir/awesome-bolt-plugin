from typing import List

from blue_options.terminal import show_usage, xtra


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    # ---
    options = "".join(
        [
            xtra("delim=+,dict.keys,dict.values,", mono=mono),
            "filename,key=<key>",
        ]
    )
    usage_1 = show_usage(
        [
            "@metadata",
            "get",
            f"[{options}]",
            "<filename.yaml>",
        ],
        "get <filename.yaml>[<key>]",
        mono=mono,
    )

    # ---
    options = "".join(
        [
            xtra("delim=+,dict.keys,dict.values,filename=<metadata.yaml>,", mono=mono),
            "key=<key>,object",
        ]
    )
    usage_2 = show_usage(
        [
            "@metadata",
            "get",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "get <object-name>/metadata[<key>]",
        mono=mono,
    )

    # ---
    options = "".join(
        [
            xtra("delim=+,dict.keys,dict.values,filename=<metadata.yaml>,", mono=mono),
            "key=<key>,path",
        ]
    )
    usage_3 = show_usage(
        [
            "@metadata",
            "get",
            f"[{options}]",
            "<path>",
        ],
        "get <path>/metadata[<key>]",
        mono=mono,
    )

    return "\n".join(
        [
            usage_1,
            usage_2,
            usage_3,
        ]
    )


def help_post(
    tokens: List[str],
    mono: bool,
) -> str:
    args = ["[--verbose 1]"]

    # ---
    options = "filename"

    usage_1 = show_usage(
        [
            "@metadata",
            "post",
            "<key>",
            "<value>",
            f"{options}",
            "<filename.yaml>",
        ]
        + args,
        "<filename.yaml>[<key>] = <value>",
        mono=mono,
    )

    # ---
    options = "".join(
        [
            "object",
            xtra(",filename=<metadata.yaml>", mono=mono),
        ]
    )

    usage_2 = show_usage(
        [
            "@metadata",
            "post",
            "<key>",
            "<value>",
            f"{options}",
            "[.|<object-name>]",
        ]
        + args,
        "<object-name>[<key>] = <value>",
        mono=mono,
    )

    # ---
    options = "".join(
        [
            "path",
            xtra(",filename=<metadata.yaml>", mono=mono),
        ]
    )

    usage_3 = show_usage(
        [
            "@metadata",
            "post",
            "<key>",
            "<value>",
            f"{options}",
            "<path>",
        ]
        + args,
        "<path>[<key>] = <value>",
        mono=mono,
    )

    return "\n".join(
        [
            usage_1,
            usage_2,
            usage_3,
        ]
    )


help_functions = {
    "get": help_get,
    "post": help_post,
}
