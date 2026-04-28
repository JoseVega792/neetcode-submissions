class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nCount = Counter(nums)

        heap = []
        for n in nCount:
            heapq.heappush(heap,(-nCount[n],n))
        
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res