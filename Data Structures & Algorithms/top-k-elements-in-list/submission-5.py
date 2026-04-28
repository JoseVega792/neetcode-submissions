class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        similarity = [[] for i in range(len(nums) + 1)]

        for x,y in counts.items():
            similarity[y].append(x)
        
        res = []
        for i in range(len(similarity) - 1,-1,-1):
            for n in similarity[i]:
                res.append(n)
                if len(res) == k:
                    return res
        