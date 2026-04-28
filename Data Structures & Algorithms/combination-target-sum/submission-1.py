class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,curr,rem):
            if rem == 0:
                res.append(curr.copy())
                return
            
            if i == len(nums) or rem < 0:
                return 
            
            curr.append(nums[i])
            backtrack(i, curr, rem - nums[i])

            curr.pop()
            backtrack(i + 1, curr, rem)
        backtrack(0,[],target)
        return res