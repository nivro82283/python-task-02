"""Extend the notebook PostOffice with unread-message access and search."""


class PostOffice:
    """Store messages per recipient, keeping urgent messages first.

    Args:
        usernames: Iterable of mailbox names.

    Attributes:
        message_id: Last assigned message identifier.
        boxes: Mailboxes containing both read and unread messages.
    """

    def __init__(self, usernames):
        """Create empty mailboxes and initialize the message counter."""
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, *, title=""):
        """Send a message and return its ID; unknown recipients raise KeyError.

        The keyword-only title and read flag extend the notebook's message format.
        Existing calls with an optional fourth urgent argument remain valid.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        details = {"id": self.message_id, "body": message_body,
                   "sender": sender, "title": title, "read": False}
        if urgent:
            user_box.insert(0, details)
        else:
            user_box.append(details)
        return self.message_id

    def read_inbox(self, username, count=None):
        """Return and mark the first count unread messages, or all if omitted.

        Negative counts raise ValueError; noninteger counts raise TypeError.
        An unknown username raises KeyError. Read messages remain searchable.
        """
        messages = self.boxes[username]
        if count is not None:
            if not isinstance(count, int):
                raise TypeError("Message count must be an integer.")
            if count < 0:
                raise ValueError("Message count must not be negative.")
        unread = [message for message in messages if not message.get("read", False)]
        selected = unread if count is None else unread[:count]
        for message in selected:
            message["read"] = True
        return selected

    def search_inbox(self, username, text):
        """Return all messages containing text in title or body, case-sensitively.

        Search includes read messages and does not change their read status.
        An unknown username raises KeyError.
        """
        return [message for message in self.boxes[username]
                if text in message.get("title", "") or text in message["body"]]


def sent_turtle():
    """Demonstrate sending, reading and searching messages."""
    office = PostOffice(["Niv", "Dana"])
    office.send_message("Niv", "Dana", "Hello!", title="Greeting")
    print(office.read_inbox("Dana"))
    print(office.read_inbox("Dana"))
    print(office.search_inbox("Dana", "Greeting"))


if __name__ == "__main__":
    sent_turtle()
