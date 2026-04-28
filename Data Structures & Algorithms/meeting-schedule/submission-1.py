"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i:i.start)
        stack = [intervals[0]]
        for i in intervals[1:]:
            if stack[-1].end > i.start:
                return False
            stack.append(i)
        return True