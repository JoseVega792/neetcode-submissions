class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        currMax = float('-inf')
        l, r = 0, k - 1 
        heap = []
        while k:
            heap.append((-1 * nums[k - 1], k - 1))
            k -= 1
        heapq.heapify(heap)
        while r < len(nums):
            while heap:
                val, ind = heapq.heappop(heap)
                val = -1 * val
                if ind >= l and ind <= r:
                    res.append(val)
                    if ind >= (l + 1) and ind <= (r + 1):
                        val = -1 * val
                        heapq.heappush(heap, (val,ind))
                    break
            l += 1
            r += 1
            if r < len(nums):
                heapq.heappush(heap, (-1 * nums[r],r))
        return res




