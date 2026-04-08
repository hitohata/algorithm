class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmin, kmax = 1, max(piles)

        k = kmax + 1

        while kmin <= kmax:
            m = kmin + (kmax - kmin) // 2
            
            if self.can_eat(m, piles, h):
                k = m
                kmax = m - 1
            else:
                kmin = m + 1
        
        return k

                

    def can_eat(self, k: int, piles: List[int], h: int):
        sum = 0
        for pile in piles:
            sum += round(pile / k)
        
        return sum <= h
        