class Solution:
    def compute(self, stack, ch):
        left, right = stack[-2], stack[-1]
        stack.pop()
        stack.pop()
        print(left, right)
        if ch == '+':
            return left + right
        elif ch == '-':
            return left - right
        elif ch == '*':
            return left * right
        else:
            return int(left / right)
    
    def evalRPN(self, tokens: List[str]) -> int:
        operation = "+-*/"
        stack = []
        for ch in tokens:
            if ch not in operation:
                stack.append(int(ch))
            else:
                val = self.compute(stack, ch)
                stack.append(val)
        
        return stack[-1]
                