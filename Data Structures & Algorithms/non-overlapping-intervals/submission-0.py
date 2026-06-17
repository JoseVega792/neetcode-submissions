class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prev = intervals[0][1]
        for x,y in intervals[1:]:
            if prev > x:
                res += 1
                prev = min(prev, y)
            else:
                prev = y
        return res