class Solution:
    def calcDistance(self, interval):
        return interval[1] - interval[0] + 1
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}

        for q in sorted(queries):
            heap = []
            i = 0
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (self.calcDistance(intervals[i]), i))
                i += 1
            while heap and not (intervals[heap[0][1]][1] >= q and intervals[heap[0][1]][0] <= q):
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        return [res[q] for q in queries] 
            
                