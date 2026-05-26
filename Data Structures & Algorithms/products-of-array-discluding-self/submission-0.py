class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, z_count = 1, 0

        for num in nums:
            if num == 0:
                z_count += 1
            else:
                prod = prod * num
        if z_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if z_count:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c

        return res