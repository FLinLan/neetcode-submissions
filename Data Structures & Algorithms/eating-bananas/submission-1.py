class Solution:
    def totalHours(self, piles, mid):
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)
        return hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on the possible pile rate
        L, R = 1, max(piles)
        ans = float('inf')
        while L <= R:
            mid = (L + R) // 2
            if self.totalHours(piles, mid) <= h:
                ans = min(ans, mid)
                R = mid - 1
            else:
                L = mid + 1
        
        return ans