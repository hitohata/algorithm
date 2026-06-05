class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w = 0
        l, r = 0, len(heights) - 1     
        
        while l < r:
            width = r - l
            l_h = heights[l]
            r_h = heights[r]
            
            if l_h <= r_h:
                t = l_h * width
                w = max(w, t)
                l += 1
            else:
                t = r_h * width
                w = max(w, t)
                r -= 1
        
        return w