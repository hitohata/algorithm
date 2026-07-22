class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        ans = [-1, -1]
        
        while l < r:
            if numbers[r] > target:
                r -= 1
                continue
            
            s = numbers[l] + numbers[r]
            
            if s == target:
                ans = [l + 1, r + 1]
                break

            if s > target:
                r -= 1
            else:
                l += 1
        
        return ans