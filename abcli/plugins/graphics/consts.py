import os
from abcli.modules import host
from . import NAME
from abcli import logging
import logging

logger = logging.getLogger(__name__)

screen_width = None
screen_height = None

# try:
if True:
    if host.is_rpi():
        if not host.is_headless():
            # https://stackoverflow.com/a/14124257
            screen = os.popen("xrandr -q -d :0").readlines()[0]
            screen_width = int(screen.split()[7])
            screen_height = int(screen.split()[9][:-1])
    elif host.is_mac():
        success, output = host.shell(
            "system_profiler SPDisplaysDataType |grep Resolution",
            clean_after=True,
            return_output=True,
        )
        output = [thing for thing in output if thing]
        if success and output:
            screen_width, screen_height = [
                int(thing) for thing in output[-1].split() if thing.isnumeric()
            ]

    else:
        from gi.repository import Gdk

        screen = Gdk.Screen.get_default()
        geo = screen.get_monitor_geometry(screen.get_primary_monitor())
        screen_width = geo.width
        screen_height = geo.height
# except:
#    logger.error(f"{NAME}: Failed.")

if screen_height is None or screen_width is None:
    logger.error(f"{NAME}: screen size not found.")
    screen_height = 480
    screen_width = 640

logger.info(f"{NAME}: {screen_height}x{screen_width}")
