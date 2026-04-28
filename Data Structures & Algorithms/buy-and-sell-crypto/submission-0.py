class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = float('inf')
        for p in prices:
            minVal = min(p,minVal)
            res = max(res, p - minVal)
        return res