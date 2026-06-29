class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l <= r:
            if l == r:
                return l

            m = (r - l) // 2 + l

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
