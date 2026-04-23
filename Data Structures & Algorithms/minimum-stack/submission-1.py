class MinStack:
    def __init__(self):
        self.stack = [] # (min_val, curr_val)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return 
        
        if val < self.stack[-1][0]:
            self.stack.append((val, val))
        else:
            self.stack.append((self.stack[-1][0], val))

    def pop(self) -> None:
        if self.stack: self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1] if self.stack else 0

    def getMin(self) -> int:
        return self.stack[-1][0] if self.stack else 0
        
