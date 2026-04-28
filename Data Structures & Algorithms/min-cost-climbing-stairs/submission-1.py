class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, sec = 0, 0
        for i in range(1, len(cost)):
            temp = sec
            sec = min(first + cost[i - 1],sec + cost[i])
            first = temp
        return sec