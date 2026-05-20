class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for c in range(m - 1):
            for r in range(1, n):
                row[r] = row[r - 1] + row[r]
        
        return row[n - 1]