class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1
        
        heap = []

        for num in d.keys():
            heapq.heappush(heap, (d[num], num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        
        