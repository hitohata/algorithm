class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        
        c = 0

        while c < m:
            for r in range(n):
                if r == 0:
                    if c == 0:
                        row[r] = 1
                        continue
                    else:
                        row[r] = row[r]
                else:
                    row[r] = row[r - 1] + row[r]
            
            c += 1
        
        return row[n - 1]