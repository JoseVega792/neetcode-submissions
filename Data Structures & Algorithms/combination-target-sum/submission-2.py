class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def search(arr=[], i = 0, curr = 0):
            if curr == target:
                res.append(arr.copy())
                return
            elif i > len(nums)-1:
                return
            elif curr > target:
                return
            
            #Add num
            arr.append(nums[i])
            curr += nums[i]
            search(arr, i, curr)

            # Continue without adding
            if arr:
                arr.pop()
            curr -= nums[i]
            search(arr, i + 1, curr)
        search()
        return res