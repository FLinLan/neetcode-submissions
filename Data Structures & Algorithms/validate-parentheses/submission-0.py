class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if stack and ch == ')' and stack[-1] == '(':
                stack.pop()
                continue
            elif stack and ch == '}' and stack[-1] == '{':
                stack.pop()
                continue
            elif stack and ch == ']' and stack[-1] == '[':
                stack.pop()
                continue
            stack.append(ch)

        return len(stack) == 0