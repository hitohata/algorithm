from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        
        if root:
            queue.append(root)
        ans = []
        while len(queue) > 0:
            same_level = []
            for el in range(len(queue)):
                front = queue.popleft()
                same_level.append(front.val)

                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)

            ans.append(same_level)
        
        return ans
            
        

        
        