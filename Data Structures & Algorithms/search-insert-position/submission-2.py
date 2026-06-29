class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums)

        while l <= r:
            if l == r:
                if l == 0:
                    return 0
                if r == len(nums):
                    return len(nums)
                return l

            m = (r - l) // 2 + l

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        