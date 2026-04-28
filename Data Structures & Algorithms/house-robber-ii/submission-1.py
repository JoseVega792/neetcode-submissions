class Solution:

    def executeRob(self, nums: List[int]):
        first, sec = 0, 0
        for n in nums:
            temp = max(first + n, sec)
            first = sec
            sec = temp
        return sec


    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.executeRob(nums[1:]), self.executeRob(nums[:-1]))