# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            ll = dfs(root.left)
            lr = dfs(root.right)
            
            self.res = max(self.res, ll + lr)

            return 1 + max(ll, lr)
        
        dfs(root)
        return self.res