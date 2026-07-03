class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxVal = 1
        minVal = 1
        for n in nums:
            temp = n * maxVal
            maxVal = max(temp, n * minVal, n)
            minVal = min(temp, n * minVal, n)
            res = max(maxVal, res)
        return res