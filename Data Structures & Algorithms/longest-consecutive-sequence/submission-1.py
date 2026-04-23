class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for n in nums:
            # if n-1 in num_set: continue
            k, length = n, 1
            while k+1 in num_set:
                length += 1
                k += 1
            ans = max(ans, length)
        
        return ans
