class Solution:
    def trap(self, height: List[int]) -> int:
        prefixL, prefixR = [0], [0]

        maxL, maxR = 0, 0
        N = len(height)
        for i in range(N):
            maxL = max(height[i], maxL)
            maxR = max(height[N-i-1], maxR)
            prefixL.append(maxL)
            prefixR.append(maxR)
        
        prefixR.reverse()
        ans = 0
        for i in range(N):
            capped = min(prefixL[i], prefixR[i])
            if capped - height[i] > 0:
                ans += (capped - height[i])
        
        return ans
                