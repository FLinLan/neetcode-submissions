class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagram[key].append(s)
        
        ans = []
        for val in anagram.values():
            sublist = []
            for s in val:
                sublist.append(s)
            ans.append(sublist)
        return ans
            