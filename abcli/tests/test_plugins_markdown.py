from abcli.string import random_
from abcli.plugins.markdown import generate_table


def test_generate_table(repo_names: bool):
    assert generate_table([random_() for _ in range(50)], col=4)
