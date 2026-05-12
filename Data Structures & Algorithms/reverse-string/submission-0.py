class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        
        for i in range(len(s) // 2):
            tmp = s[r - i]
            s[r - i] = s[i]
            s[i] = tmp
        
        return r
