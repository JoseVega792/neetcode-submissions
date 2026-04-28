class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            curr = (r + l) // 2

            total = 0
            for p in piles:
                total += math.ceil(float(p)/curr)
            if total <= h:
                res = curr
                r = curr - 1
            else:
                l = curr + 1
        return res
