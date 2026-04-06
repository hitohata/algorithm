class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for i in nums:
            colors[i] += 1
        
        i = 0

        for ind, ci in enumerate(colors):
            for j in range(ci):
                nums[i] = ind
                i += 1
                
