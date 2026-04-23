class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums = temperatures.copy()
        stack = []
        ans = [0] * len(nums)

        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)
        
        return ans
                