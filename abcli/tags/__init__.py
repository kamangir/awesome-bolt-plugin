from functools import reduce
import os
import random
import re
from ..options import Options
from ..table import Table
from .. import logging
import logging

logger = logging.getLogger(__name__)

from .. import *

name = f"{shortname}.tags"


create_command = [
    "keyword VARCHAR(256) NOT NULL",
    "tag VARCHAR(4096) NOT NULL",
    "value BIT NOT NULL",
]


def get(keyword):
    """get tags for keyword.

    Args:
        keyword (str): keyword.

    Returns:
        bool: List(str).
    """
    table = Table(name="tags")

    if not table.connect(create_command):
        return []

    success, output = table.execute(
        "SELECT t.tag,t.value "
        f"FROM {table.name} t "
        "INNER JOIN ( "
        "SELECT tag, MAX(timestamp) AS max_timestamp "
        f"FROM {table.name} "
        f'WHERE keyword="{keyword}" GROUP BY tag '
        ") tm "
        "ON t.tag=tm.tag AND t.timestamp=tm.max_timestamp "
        f'WHERE keyword="{keyword}";',
        commit=False,
        returns_output=True,
    )

    if success:
        success = table.disconnect()

    if not success:
        return []

    return sorted([thing[0] for thing in output if thing[1] == b"\x01"])


def search(
    tags,
    after="",
    before="",
    count=-1,
    host=-1,
    return_timestamp=False,
    shuffle=False,
):
    """search.

    Args:
        tags (List(str)): list of tags.
        after (str, optional): include keywords after and including. Defaults to "".
        before (str, optional): include keywords before and including. Defaults to "".
        count (int, optional): keyword count to return. Defaults to -1.
        host (int, optional): limit to/exclude/ignore (1/0/-1) hosts. Defaults to -1.
        return_timestamp (bool, optional): return timestamp. Defaults to False.
        shuffle (bool, optional): shuffle output. Defaults to False.

    Returns:
        List(str): list of keywords.
    """
    if isinstance(tags, str):
        tags = tags.split(",")

    included_tags = []
    excluded_tags = []
    for tag in tags:
        if tag:
            if tag[0] in "~-!":
                excluded_tags += [tag[1:]]
            else:
                included_tags += [tag]

    table = Table(name="tags")

    table.connect(create_command)

    list_of_keywords = None
    timestamp = {}
    for tag in included_tags:
        query = (
            "SELECT t.keyword,t.value,t.timestamp "
            "FROM abcli.tags t "
            "INNER JOIN ( "
            "SELECT keyword, MAX(timestamp) AS max_timestamp "
            "FROM abcli.tags "
            'WHERE tag="{}" '.format(tag) + "GROUP BY keyword "
            ") tm "
            "ON t.keyword=tm.keyword AND t.timestamp=tm.max_timestamp "
            'WHERE tag="{}"; '.format(tag)
        )

        success, output = table.execute(
            query,
            commit=False,
            return_results=True,
        )
        if not success:
            list_of_keywords = []
            break

        list_of_keywords_ = [thing[0] for thing in output if thing[1] == b"\x01"]

        if return_timestamp:
            for thing in output:
                if thing[1] == b"\x01":
                    timestamp[thing[0]] = thing[2]

        if list_of_keywords is None:
            list_of_keywords = list_of_keywords_
        else:
            list_of_keywords = [
                keyword for keyword in list_of_keywords if keyword in list_of_keywords_
            ]

    table.disconnect()

    list_of_keywords = [] if list_of_keywords is None else sorted(list_of_keywords)

    if after:
        list_of_keywords = [keyword for keyword in list_of_keywords if keyword >= after]

    if before:
        list_of_keywords = [
            keyword for keyword in list_of_keywords if keyword <= before
        ]

    excluded_keywords = reduce(
        lambda x, y: x + y,
        [
            search(
                tag,
                after=after,
                before=before,
                count=-1,
                host=host,
            )
            for tag in excluded_tags
        ],
        [],
    )

    list_of_keywords = [
        keyword for keyword in list_of_keywords if keyword not in excluded_keywords
    ]

    if shuffle:
        random.shuffle(list_of_keywords)

    p = re.compile("([0-9]{13}|(0|1)[0-9,a-z]{15}|i-[0-9,a-z]{17})")
    if host == 1:
        list_of_keywords = [keyword for keyword in list_of_keywords if p.match(keyword)]
    if host == 0:
        list_of_keywords = [
            keyword for keyword in list_of_keywords if not p.match(keyword)
        ]

    if count > 0:
        list_of_keywords = list_of_keywords[-count:]
    elif count != -1:
        list_of_keywords = []

    return (list_of_keywords, timestamp) if return_timestamp else list_of_keywords


def set_(keyword, tags):
    """set tags for keyword.

    Args:
        keyword (str): keyword.
        tags (List(str)): list of strings or string.

    Returns:
        bool: success.
    """
    table = Table(name="tags")

    if isinstance(tags, list):
        tags = ",".join(tags)
    if isinstance(tags, str):
        tags = Options(tags)

    if not table.connect(create_command):
        return False

    tags = {tag.strip(): value for tag, value in tags.items()}

    success = True
    for tag in tags:
        if not table.insert(
            "keyword,tag,value".split(","),
            [keyword, tag, 1 if tags[tag] else 0],
        ):
            success = False
        else:
            if tags[tag]:
                logger.info(f"{keyword} += #{tag}.")
            else:
                logger.info(f"{keyword} -= #{tag}.")

    if not table.disconnect():
        return False

    return success
