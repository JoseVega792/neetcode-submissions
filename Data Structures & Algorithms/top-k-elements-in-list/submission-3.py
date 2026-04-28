class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(-counts[k],k) for k in counts]
        heapq.heapify(heap)
        res = []
        while k and heap:
            curr = heapq.heappop(heap)
            res.append(curr[-1])
            k -= 1
        return res