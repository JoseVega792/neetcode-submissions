class Solution:
    def rob(self, nums: List[int]) -> int:
        first, sec = 0,0
        for n in nums:
            temp = max(first + n, sec)
            first = sec
            sec = temp
        return sec