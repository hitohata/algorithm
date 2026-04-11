class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            if d.get(i):
                d[i] = d[i] + 1
            else:
                d[i] = 1
        
        max_count = -math.inf
        ans = -math.inf
        for k,v in d.items():
            if v > max_count:
                max_count = v
                ans = k
        return ans