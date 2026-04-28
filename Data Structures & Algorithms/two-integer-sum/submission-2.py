class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i,n in enumerate(nums):
            remaining = target - n
            if n in remainders:
                return [remainders[n],i]
            remainders[remaining] = i
        return [-1,-1]