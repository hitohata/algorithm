class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev, cur = 0, 1
        s = numbers[0]

        while s < target and cur < len(numbers) - 1:
            if prev != cur:
                s += numbers[cur]
            prev = cur
            cur += 1
            
        return numbers[0:cur]