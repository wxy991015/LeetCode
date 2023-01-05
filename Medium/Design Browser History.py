# version 1 - Does not work properly
"""
class BrowserHistory:
    broswer_history = []
    current_location = 0
    def __init__(self, homepage: str):
        self.homepage = homepage
        self.broswer_history.append(homepage)

    def visit(self, url: str) -> None:
        self.homepage = url
        self.broswer_history.append(url)
        self.current_location = len(self.broswer_history) - 1

    # back and forward function need to modify
    def back(self, steps: int) -> str:
        steps = min(self.current_location, steps)
        self.current_location -= steps
        print(self.current_location)
        return self.broswer_history[self.current_location]

    def forward(self, steps: int) -> str:
        steps = min(len(self.broswer_history) - 1 - self.current_location, steps)
        self.current_location += steps
        return self.broswer_history[self.current_location]
"""

# version 2 - Work properly by using stack
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.step = 1

    def visit(self, url: str) -> None:
        # use stack => pop history until it reaches the last visit
        while len(self.history) > self.step:
            self.history.pop()
        self.history.append(url)
        self.step = len(self.history)

    def back(self, steps: int) -> str:
        if steps < self.step:
            self.step -= steps
        else:
            # go back to the beginning of the browser history (equal inclusive)
            self.step = 1
        return self.history[self.step-1]
                            
    def forward(self, steps: int) -> str:
        if steps + self.step < len(self.history):
            self.step += steps
        else:
            # go forward to the end of the browswer history
            self.step = len(self.history)
        return self.history[self.step-1]