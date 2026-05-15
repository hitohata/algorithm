class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 1
        res = 1

        while r < len(s):
            if s[r] in s[l:r]: 
                res = max(res, r - l)
                l += 1
                r = l + 1
                continue
            r += 1
            res = max(res, r - l)

        return res