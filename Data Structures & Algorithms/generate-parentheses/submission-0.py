class Solution:        
    def generateParenthesis(self, n: int) -> List[str]:
        ans, path = [], []
        
        def backtrack(opened, closed):
            if opened > n or closed > n or closed > opened:
                return
            if opened == n and closed == n:
                ans.append("".join(path.copy()))
                return
            
            path.append('(')
            backtrack(opened+1, closed)
            path.pop()

            path.append(')')
            backtrack(opened, closed+1)
            path.pop()
        
        backtrack(0, 0)
        return ans
        