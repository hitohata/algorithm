class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w = 0
        l, r = 0, len(heights) - 1     
        
        while l < r:
            width = r - l
            t = min(heights[l], heights[r]) * width
            w = max(w, t)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return w