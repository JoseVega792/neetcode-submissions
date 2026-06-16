class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        time = 0
        # count, nextInd
        queue = deque([])
        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                curr = 1 + heapq.heappop(heap)
                if curr:
                    queue.append([curr, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time