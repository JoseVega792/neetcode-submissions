class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)
        res = 0
        for n in contains:
            lowerCount = 0
            curr = n
            while curr - 1 in contains:
                curr -= 1
                lowerCount += 1
            upperCount = 0
            curr = n
            while curr + 1 in contains:
                curr += 1
                upperCount += 1
            res = max(res,lowerCount + upperCount + 1)
        return res