class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # stack of indices of min
        self.min = []

    def push(self, val: int) -> None:
        if not self.min or self.stack[self.min[-1]] > val:
            self.min.append(len(self.stack))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()