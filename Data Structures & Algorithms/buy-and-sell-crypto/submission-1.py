class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        minVal = float('inf')
        for p in prices:
            minVal = min(minVal, p)
            res = max(res, p - minVal)
        return int(res)