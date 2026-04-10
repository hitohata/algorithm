# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        slist = []
        
        self.dst(root, slist, k)

        return slist[k - 1]

    def dst(self, root, slist, k):
        if not root:
            return None

        if len(slist) == k:
            return None
        
        self.dst(root.left, slist, k)
        slist.append(root.val)
        self.dst(root.right, slist, k)       
                

