class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res =  r
        while l <= r:
            mid = (l + r) // 2
            newP = 0
            for p in piles:
                newP += math.ceil(float(p) / mid)
            
            if newP <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            