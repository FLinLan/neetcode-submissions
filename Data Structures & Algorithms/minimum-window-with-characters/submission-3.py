class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        the seen variable is the size of the map
        not the size of t
        we want to implement a mechanism that allow us to
        pick out characters that we need, and disregard the
        extraneous characters
        we can do so by check if s_map[ch] <= t_map[ch] for sufficient
        characters
        """
        if len(s) < len(t) or t == "": return ""
        s_map, t_map = Counter(), Counter(t)

        L, R = 0, 0
        ans = [float('inf'), L, R]

        seen, matching = 0, len(t_map)
        for R in range(len(s)):
            chR = s[R]
            s_map[chR] += 1
            if chR in t_map and s_map[chR] == t_map[chR]:
                seen += 1
            while L <= R and seen == matching:
                if ans[0] > (R-L+1):
                    ans[0] = (R-L+1)
                    ans[1] = L
                    ans[2] = R
                chL = s[L]
                s_map[chL] -= 1
                if chL in t_map and s_map[chL] < t_map[chL]:
                    seen -= 1
                L += 1
        
        L, R = ans[1], ans[2]
        return s[L:R+1] if ans[0] != float('inf') else ""
