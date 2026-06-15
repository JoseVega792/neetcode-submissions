class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)
            if first == second:
                continue
            elif first < second:
                heapq.heappush(heap, -(second - first))
            else:
                heapq.heappush(heap, -(first - second))
        return -heap[0] if len(heap) > 0 else 0