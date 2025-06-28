class MinStack:

    def __init__(self):
        self.stack = []       # Main stack
        self.min_stack = []   # Stack to track current min at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new min (either val or current min)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
