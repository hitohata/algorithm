from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ans = []

        queue.append(root)

        while len(queue) > 0:
            right = queue[-1]
            ans.append(right.val)

            for i in range(len(queue)):
                left = queue.popleft()
                if left.left:
                    queue.append(left.left)
                if left.right:
                    queue.append(left.right)
        
        return ans