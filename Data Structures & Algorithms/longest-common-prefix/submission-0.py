class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []

        for s in strs[0]:
            ans.append(s)

        for targ in strs[1:]:
            ans = ans[:len(targ)]
            for i, s in enumerate(targ):
                if i < len(ans) and ans[i] != s:
                    ans = ans[:i]
                    break
                    
        return "".join(ans)

        

        