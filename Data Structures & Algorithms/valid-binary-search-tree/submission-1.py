# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        preorder : root -> left -> right
        inorder : left -> root -> right
        postorder : left -> right -> root
        """

        # a validate bst will have values in ascending order 
        # when traversed in an inorder fashion

        inorder = [] # left -> root -> right

        def dfs(root):
            if not root: return

            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)

        dfs(root)

        for i in range(1, len(inorder)):
            if inorder[i-1] >= inorder[i]:
                return False
        
        return True
