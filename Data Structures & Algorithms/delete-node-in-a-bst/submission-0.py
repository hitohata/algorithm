# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            minNode = findMinNode(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)

        return root 
        
def findMinNode(root: Optional[TreeNode]):
    curr = root
    
    while curr and curr.left:
        curr = curr.left
    
    return curr
    
    
    