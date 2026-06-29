class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def cal(i: int, bought: bool):
            if i >= len(prices):
                return 0
            
            res = cal(i + 1, bought)

            if bought:
                res = max(res, prices[i] + cal(i + 1, False))
            else:
                res = max(res, -prices[i] + cal(i + 1, True))
            
            return res

        return cal(0, False)