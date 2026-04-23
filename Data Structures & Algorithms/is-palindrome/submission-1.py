class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L <= R:
            chL, chR = s[L], s[R]
            if not chR.isalnum():
                R -= 1
            elif not chL.isalnum():
                L += 1
            else:
                if chL.lower() == chR.lower():
                    L += 1
                    R -= 1
                else:
                    return False
        return True
                    