class Solution:
    def rob(self, nums: List[int]) -> int:
        first,sec = 0,0
        for n in nums:
            temp = first
            first = max(first,sec + n)
            sec = temp
        return first
        