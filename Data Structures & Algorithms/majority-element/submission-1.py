class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max_count = -math.inf
        ans = -math.inf

        for i in nums:
            d[i] += 1
            if d[i] > max_count:
                ans = i
                max_count = d[i]

        return ans