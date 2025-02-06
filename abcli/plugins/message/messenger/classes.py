from typing import List, Tuple

from abcli.plugins.message.classes import Message
from abcli.plugins.message.queue.classes import MessageQueue


class Messenger:
    def __init__(self, recipients=[]):
        self.recipients = recipients
        self._queue = {}

    def queue(self, name: str) -> MessageQueue:
        if name not in self._queue:
            self._queue[name] = MessageQueue(name)

        return self._queue[name]

    def request(
        self,
        recipients=None,
        count: int = 10,
        delete: bool = False,
    ) -> Tuple[bool, List[Message]]:

        output = []
        success = True

        if recipients is None:
            recipients = self.recipients

        if isinstance(recipients, str):
            recipients = recipients.split(",")

        for recipient in recipients:
            success_, messages = self.queue(recipient).request(
                count=count,
                delete=delete,
            )

            if not success_:
                success = False
                break

            if messages:
                output.extend(messages)

        return success, output
