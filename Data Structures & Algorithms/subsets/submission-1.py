class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(ind):
            if ind >= len(nums):
                res.append(curr.copy())
                return 
            
            curr.append(nums[ind])
            backtrack(ind + 1)

            curr.pop()
            backtrack(ind + 1)
        backtrack(0)
        return res