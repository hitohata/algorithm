class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l, r = 0, 0
        count = len(nums)

        while r < len(nums):
            if nums[r] == val:
                count -= 1
            else:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return count