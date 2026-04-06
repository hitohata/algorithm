class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        removed_duplicate = set(nums)
        return len(removed_duplicate) != len(nums)