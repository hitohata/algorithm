class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in pair:
                pair[target - num] = i
            else:
                return [pair[num], i]