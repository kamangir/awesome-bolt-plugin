from blue_options import host

from abcli import env
from abcli.plugins.message.messenger.classes import Messenger


instance = Messenger(
    recipients=list(
        set(
            [
                "public",
                host.get_name(),
            ]
            + [thing for thing in env.ABCLI_MESSENGER_RECIPIENTS.split(",") if thing]
        )
    )
)
