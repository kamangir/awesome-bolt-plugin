import argparse
from .functions import *
from ... import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(name)
parser.add_argument(
    "task",
    type=str,
    default="terraform",
    help="poster/terraform",
)
parser.add_argument(
    "--filename",
    type=str,
    default="background.jpg",
    help="",
)
parser.add_argument(
    "--is_lite",
    type=str,
    default="false",
    help="true/false",
)
parser.add_argument(
    "--target",
    type=str,
    default="none",
    help="lxde/mac/rpi/ubuntu",
)
parser.add_argument(
    "--user",
    type=str,
    default="user",
    help="",
)
args, _ = parser.parse_known_args()

success = False
if args.task == "poster":
    success = poster(args.filename)
elif args.task == "terraform":
    logger.info("terraforming {}".format(args.target))

    if args.target == "lxde":
        success = lxde(args.user)
    elif args.target == "mac":
        success = mac(args.user)
    elif args.target == "rpi":
        success = rpi(args.user, args.is_lite == "true")
    elif args.target == "ubuntu":
        success = ubuntu(args.user)
    else:
        logger.error(f"-{name}: {args.target}: target not found.")
else:
    logger.error(f"-{name}: {args.task}: command not found.")

if not success:
    logger.error(f"-{name}: {args.task}: failed.")
