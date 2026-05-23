class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)
        res = 0
        for n in contains:
            if n - 1 not in contains:
                curr = n
                count = 1
                while curr + 1  in contains:
                    curr += 1
                    count += 1
                res = max(res, count)
        return res