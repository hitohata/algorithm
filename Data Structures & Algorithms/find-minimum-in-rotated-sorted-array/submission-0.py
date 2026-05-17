class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            left, right = nums[l], nums[r]
            if left < right:
                res = min(res, left)
                break

            m = l + (r - l) // 2

            res = min(res, nums[m])

            if nums[m] >= left:
                l = m + 1
            else:
                r = m - 1


        return res