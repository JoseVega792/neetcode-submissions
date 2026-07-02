class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = nums[0]
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            res = max(res, currSum)
        return res