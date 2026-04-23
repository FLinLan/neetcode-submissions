class MinStack:
    def __init__(self):
        self.min_val = []  # Stack to track minimum values
        self.stack = []    # Stack to store the actual values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Update min_val with the new minimum
        if not self.min_val:
            self.min_val.append(val)
        else:
            self.min_val.append(min(val, self.min_val[-1]))
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_val.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else 0
        
    def getMin(self) -> int:
        return self.min_val[-1] if self.min_val else 0