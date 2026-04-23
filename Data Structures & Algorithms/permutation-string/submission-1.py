class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_map, s2_map = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            i1 = ord(s1[i]) - ord('a')
            i2 = ord(s2[i]) - ord('a')
            s1_map[i1] += 1 
            s2_map[i2] += 1 

        start, end = len(s1), len(s2)
        L = 0
        for R in range(start, end):
            if s1_map == s2_map:
                return True
            chR, chL = s2[R], s2[L]
            indR = ord(s2[R]) - ord('a')
            indL = ord(s2[L]) - ord('a')
            s2_map[indR] += 1
            s2_map[indL] -= 1
            L += 1
        
        return s1_map == s2_map
