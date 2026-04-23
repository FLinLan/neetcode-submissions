class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        L, R = 0, 0
        ans = 0
        while R < len(s):
            chR = s[R]
            count[chR] += 1
            while count[chR] > 1:
                chL = s[L]
                count[chL] -= 1
                if count[chL] <= 0:
                    del count[chL]
                L += 1
            ans = max(ans, R-L+1)
            R += 1
        return ans
            