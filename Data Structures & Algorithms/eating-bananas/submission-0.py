class Solution:
    def totalHours(self, piles, mid):
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)
        return hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        binary search on a valid rate that can finish all bananas
        runtime should be O(nlogk) where k is the minimum rate and n is the 
        size of the piles array
        space is O(1)
        how do i determine the maximum possible rate?
        """        
        ans = float('inf')
        L, R = 1, max(piles)
        while L <= R:
            mid = (L + R) // 2
            if self.totalHours(piles, mid) <= h:
                ans = min(ans, mid)
                R = mid - 1
            else:
                L = mid + 1
        
        return ans
            