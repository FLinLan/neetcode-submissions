class Solution:
    def compute(self, stack, op):
        left, right = stack[-2], stack[-1]
        stack.pop()
        stack.pop()
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        else:
            return int(left / right)
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = "+-*/"
        for op in tokens:
            if op in operation:
                val = self.compute(stack, op)               
                stack.append(val) 
            else:
                stack.append(int(op))
        
        return stack[-1]
