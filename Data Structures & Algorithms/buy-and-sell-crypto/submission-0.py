class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        R, L = 0, 0
        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
            diff = prices[R] - prices[L]
            ans = max(ans, diff)
            R += 1
        
        return ans
            