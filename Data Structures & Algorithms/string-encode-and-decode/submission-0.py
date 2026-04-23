class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        print(s)
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1 # skip over the delimiter
            ans.append(s[i:i+int(num)])
            i += int(num)
            # 4#neet4#code4#love3#you
        return ans
