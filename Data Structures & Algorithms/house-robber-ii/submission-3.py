class Solution:

    def simRob(self, nums: List[int]) -> int:
        first, second = 0,0
        for i in range(len(nums)):
            temp = max(first + nums[i], second)
            first = second
            second = temp
        return second

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.simRob(nums[1:]), self.simRob(nums[:len(nums) - 1]))