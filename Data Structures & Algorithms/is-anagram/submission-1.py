class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = Counter(s), Counter(t)
        return smap == tmap