import argparse
from . import *
from abcli import logging
import logging

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="status|validate",
)
args = parser.parse_args()

success = False
if args.task == "status":
    success = True
    print(int(get_status()))
if args.task == "validate":
    success = validate()
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
