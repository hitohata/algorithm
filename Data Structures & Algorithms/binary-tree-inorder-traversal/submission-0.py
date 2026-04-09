# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        dfs(root, output)
        return output
        
def dfs(root: Optional[TreeNode], output: List[int]):
    if not root:
        return;
    
    dfs(root.left, output)
    output.append(root.val)
    dfs(root.right, output)
        
        