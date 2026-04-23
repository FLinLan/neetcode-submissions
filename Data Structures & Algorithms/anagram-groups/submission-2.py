class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                key[index] += 1
            anagrams[tuple(key)].append(s)
        
        return anagrams.values()
            