class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,3]
        
        """
        path, ans = [], []
        visit = set()
        def backtrack():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for n in nums:
                if n not in visit:
                    path.append(n)
                    visit.add(n)
                    backtrack()
                    path.pop()
                    visit.remove(n)
            
            return
        
        backtrack()
        return ans
                