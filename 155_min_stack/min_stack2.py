class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        minimum = self.mini[-1] if self.mini else x
        if x <= minimum:
            self.mini.append(x)

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.mini[-1]:
            self.mini.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.mini[-1]

"""
Use an extra stack to keep track of the current minimum value.

If a new element is larger than the current minimum, we do not need to
push it on to the min stack. When we perform the pop operation, check
if the popped element is the same as the current minimum. If it is,
pop it off the min stack too.
"""