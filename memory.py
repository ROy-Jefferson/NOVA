class Memory:
    """
    Stores everything NOVA remembers during a session.
    """

    def __init__(self):
        self.current_document = None
        self.chat_history = []