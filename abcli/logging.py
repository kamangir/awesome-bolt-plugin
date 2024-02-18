import logging
from logging.handlers import RotatingFileHandler
import os


abcli_log_filename = os.getenv("abcli_log_filename", "abcli.log")

# Based on https://stackoverflow.com/a/22313803
logging.addLevelName(logging.INFO, "ℹ️")
logging.addLevelName(logging.DEBUG, "❓")
logging.addLevelName(logging.ERROR, "❗️")

logging_level = logging.INFO

logging.getLogger().setLevel(logging_level)

log_formatter = logging.Formatter("%(levelname)s %(asctime)s | %(name)s | %(message)s")
try:
    file_handler = RotatingFileHandler(
        abcli_log_filename,
        maxBytes=10485760,
        backupCount=10000,
    )
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(log_formatter)
    logging.getLogger().addHandler(file_handler)
except:
    pass

console_handler = logging.StreamHandler()
console_handler.setLevel(logging_level)
console_handler.setFormatter(log_formatter)
logging.getLogger().addHandler(console_handler)

logger = logging.getLogger("abcli")


def crash_report(description):
    # https://stackoverflow.com/a/10645855
    logger.error(f"crash: {description}", exc_info=1)
