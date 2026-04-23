class Solution:
    def maxCount(self, s_map):
        count = 0
        for i in range(len(s_map)):
            count = max(count, s_map[i])
        return count
    
    def characterReplacement(self, s: str, k: int) -> int:
        """
        "AAABABB" 
         you want to alwasy replace the rest of the characters
         with the character with the largest frequency
        """
        s_map = [0] * 26
        L, R = 0, 0
        ans = 0
        while R < len(s):
            chR = ord(s[R]) - ord('A')
            s_map[chR] += 1
            while L <= R and (R-L+1) - self.maxCount(s_map) > k:
                chL = ord(s[L]) - ord('A')
                s_map[chL] -= 1
                L += 1
            ans = max(ans, R-L+1)
            R += 1
        
        return ans
                          