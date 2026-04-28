class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i,n in enumerate(nums):
            remaining = target - n
            if remaining in remainders:
                return [remainders[remaining], i]
            remainders[n] = i
        return [-1,-1]