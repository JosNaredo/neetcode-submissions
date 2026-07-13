class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return self.stack

    def pop(self) -> None:
        self.stack = self.stack[0:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = min(self.stack)
        return minimum
