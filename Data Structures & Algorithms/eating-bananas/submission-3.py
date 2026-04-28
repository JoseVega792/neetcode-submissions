class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l <= r:
            curr = (l + r) // 2
            currCost = 0
            for p in piles:
                currCost += math.ceil(p / curr)
            if h >= currCost:
                res = curr
                r = curr - 1
            else:
                l = curr + 1
        return res

        