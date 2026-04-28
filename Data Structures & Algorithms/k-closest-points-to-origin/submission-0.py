class Solution:
    def distance(self, x,y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heapq.heappush(heap, (self.distance(x,y), x,y))
        print(heap)
        res = []
        while heap and k:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
        return res