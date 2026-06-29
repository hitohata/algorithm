class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l