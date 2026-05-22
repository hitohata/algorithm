# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        res = True
        
        def dfs(pt: Optional[TreeNode], qt: Optional[TreeNode]):
            nonlocal res
            if not res:
                return
            
            if not pt and qt:
                res = False
                return

            if  pt and not qt:
                res = False
                return

            if not pt and not qt:
                return
            
            if pt.val != qt.val:
                res = False
                return
            
            dfs(pt.left, qt.left)
            dfs(pt.right, qt.right)

        dfs(p, q)
        return res