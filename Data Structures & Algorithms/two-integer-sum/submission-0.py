class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n in count:
                return [count[n], i]
            else:
                count[diff] = i
                
        return [-1, -1]