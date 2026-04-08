class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1

        targetm = -1

        for i, nlist in enumerate(matrix):
            if nlist[l] <= target <= nlist[r]:
                targetm = i 
                break
    
        if targetm < 0:
            return False

        raw = matrix[targetm]

        while l <= r:
            m = l + (r - l) // 2 # for over flow

            val = raw[m]
            
            if val == target:
                return True

            if val < target:
                r = m - 1
            else:
                l = m + 1
        
        return False