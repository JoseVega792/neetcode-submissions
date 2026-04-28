class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, curr):
            nonlocal res
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            curr.pop()
            backtrack(i + 1, curr)
            return 
        backtrack(0,[])
        return res