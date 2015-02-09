class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if self.min == None:
            self.min = x
        else:
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.min:
            self.min = min(self.stack) if self.stack else None

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min