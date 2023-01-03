class Logger:
    def __init__(self):
        self.messages = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            timestamp += 10
            self.messages[message] = timestamp
            return True
        else:
            if timestamp >= self.messages[message]:
                self.messages[message] = timestamp + 10
                return True
            else:
                return False