class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        # circular queue with fixed size
        self.queue = [0] * size
        # head of circular queue, index of next element
        self.head = 0
        # sum of elements in circular queue
        self.total = 0
        # number of elements in circular queue
        self.count = 0

    def next(self, val: int) -> float:
        self.total = self.total - self.queue[self.head] + val
        self.queue[self.head] = val
        self.count = min(self.count + 1, len(self.queue))
        self.head = (self.head + 1) % (len(self.queue))
        return self.total / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)