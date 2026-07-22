class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        
        while r < len(s):
            if s[r + 1] == s[l]:
                l += 1
                r += 1
            else:
                r += 1
        
        return r - l
