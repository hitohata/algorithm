class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for ss in s:
            if ss in count:
                count[ss] = count[ss] + 1
            else:
                count[ss] = 1
        
        for ts in t:
            if ts not in count:
                return False
            
            if count[ts] == 0:
                return False

            count[ts] = count[ts] - 1

            if count[ts] == 0:
                del count[ts]
        
        return True if len(count) == 0 else False