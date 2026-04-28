class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i,n in enumerate(nums):
            curr = target - n
            if curr in diff:
                return [diff[curr],i]
            diff[n] = i
        return [-1,-1]