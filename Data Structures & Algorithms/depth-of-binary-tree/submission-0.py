# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        if root:
            queue.append(root)
        
        l = 0
        while len(queue) > 0:
            sub = []
            for t in queue:
                if t.left:
                    sub.append(t.left)
                if t.right:
                    sub.append(t.right)
            queue = sub
            
            l += 1

        return l


