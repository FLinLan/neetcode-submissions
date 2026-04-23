class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        """
        L, R = 0, len(nums) - 1 

        ans = float('inf')
        while L <= R:
            mid = (L + R) // 2
            if nums[L] <= nums[mid]:
                ans = min(ans, nums[L])
                L = mid + 1
            else:
                ans = min(ans, nums[mid])
                R = mid - 1
        
        return ans
        