from typing import List

from blue_options.terminal import show_usage

example_list = "<item-1>,<item-2>,..."


def help_list_filter(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--contains <this>]",
        "[--doesnt_contain <that>]",
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "filter",
            f"{example_list}",
        ]
        + args,
        "filter list.",
        mono=mono,
    )


def help_list_in(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "in",
            "<item>",
            f"{example_list}",
        ]
        + args,
        "True | False.",
        mono=mono,
    )


def help_list_intersect(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "intersect",
            f"{example_list}",
            f"{example_list}",
        ]
        + args,
        "intersect the two lists.",
        mono=mono,
    )


def help_list_item(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "item",
            f"{example_list}",
            "<index>",
        ]
        + args,
        "list[<index>].",
        mono=mono,
    )


def help_list_len(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "len",
            f"{example_list}",
        ]
        + args,
        "len(list).",
        mono=mono,
    )


def help_list_log(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--before <loading>]",
        "[--after <thing(s)>]",
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "log",
            f"{example_list}",
        ]
        + args,
        "log list.",
        mono=mono,
    )


def help_list_next(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "next",
            "<item>",
            f"{example_list}",
        ]
        + args,
        "item after <item> in list.",
        mono=mono,
    )


def help_list_nonempty(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "nonempty",
            f"{example_list}",
        ]
        + args,
        "non-empty items in list.",
        mono=mono,
    )


def help_list_prev(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "prev",
            "<item>",
            f"{example_list}",
        ]
        + args,
        "item before <item> in list.",
        mono=mono,
    )


def help_list_resize(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
    ]

    return show_usage(
        [
            "@list",
            "resize",
            f"{example_list}",
            "-1 | <length>",
        ]
        + args,
        "resize list.",
        mono=mono,
    )


def help_list_sort(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space | <delim>]",
        "[--unique 0|1]",
    ]

    return show_usage(
        [
            "@list",
            "sort",
            f"{example_list}",
        ]
        + args,
        "sortlist.",
        mono=mono,
    )


help_functions = {
    "filter": help_list_filter,
    "in": help_list_in,
    "intersect": help_list_intersect,
    "item": help_list_item,
    "len": help_list_len,
    "log": help_list_log,
    "next": help_list_next,
    "nonempty": help_list_nonempty,
    "prev": help_list_prev,
    "resize": help_list_resize,
    "sort": help_list_sort,
}
