class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        keep idea is to keep the monotonic order such that I can preform an extension
        """
        stack = [] # (height, index)
        ans = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                area = height * (i - index)
                ans = max(ans, area)
                start = index
            stack.append((h, start)) # (height, index)
        
        end = len(heights)
        print(stack)
        for h, i in stack:
            area = h * (end - i)
            ans = max(ans, area)
        
        return ans
