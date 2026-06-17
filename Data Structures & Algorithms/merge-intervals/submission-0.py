class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for x,y in intervals:
            if x <= res[-1][1]:
                prev = res.pop()
                res.append([min(prev[0], x), max(prev[1],y)])
            else:
                res.append([x,y])
        return res