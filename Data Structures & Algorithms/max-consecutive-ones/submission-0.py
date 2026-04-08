class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0

        for num in nums:
            if num != 1:
                prev = num
                count = 0
                continue
            
            count += 1
            ans = max(ans, count)  
        
        return ans