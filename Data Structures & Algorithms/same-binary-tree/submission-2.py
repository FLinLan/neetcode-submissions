# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        """
        p.left
        q.left

        p.right
        q.right
        traverse both trees in the same direction
        if value is not the same, return false
        if value is the same, return true
        if not root: return True # have not reached false value
        if p.val != q.val: return False
        
        """

        def dfs(p, q):
            if not q and not p: return True
            if (not q or not p) or (p.val != q.val): return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)




