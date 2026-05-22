class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remaining = {}
        for i,n in enumerate(numbers):
            remainder = target - n
            if n in remaining:
                return [remaining[n] , i + 1]
            remaining[remainder] = i + 1
        return []