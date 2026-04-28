class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i,n in enumerate(nums):
            remaining = target - n
            if n in remainder:
                return [remainder[n],i]
            remainder[remaining] = i
        return [0,0]