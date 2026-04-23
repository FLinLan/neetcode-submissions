# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None

        # we have exclusive comparisons for cases where 
        # our LCA might be p and q itself
        if root.val > p.val and root.val > q.val:
            # current value too great, search to left
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            # current value too small, search to left
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # we've founded a value that fits the recursive property of bst
            # this is our root
            return root

        
