class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        local_sum = 0
        ans = False

        def search(root: Optional[TreeNode], current_sum: int):
            nonlocal ans
            if not root:
                return
            if ans:
                return
            
            current_sum += root.val

            if not root.left and not root.right and current_sum == targetSum:
                ans = True
                return
                

            if root.left:
                search(root.left, current_sum)
            if root.right:
                search(root.right, current_sum)

            current_sum -= root.val

        search(root, 0)
        return ans