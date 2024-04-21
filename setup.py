from setuptools import setup

from abcli import NAME, VERSION, DESCRIPTION

setup(
    name=NAME,
    author="kamangir",
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.bash",
        f"{NAME}.bash.list",
        f"{NAME}.file",
        f"{NAME}.keywords",
        f"{NAME}.options",
        f"{NAME}.path",
        f"{NAME}.modules",
        f"{NAME}.modules.host",
        f"{NAME}.plugins",
        f"{NAME}.plugins.cache",
        f"{NAME}.plugins.graphics",
        f"{NAME}.plugins.gpu",
        f"{NAME}.plugins.metadata",
        f"{NAME}.plugins.storage",
        f"{NAME}.plugins.tags",
        f"{NAME}.string",
        f"{NAME}.table",
        f"{NAME}.tests",
    ],
    package_data={
        NAME: ["config.env"],
    },
)
