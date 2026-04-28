class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(arr, rem):
            results = []
            remaning = {}
            seen = set()
            for i,val in enumerate(arr):
                target = rem - val
                if val in remaning and val not in seen:
                    results.append([arr[remaning[val]], val])
                    seen.add(val)
                remaning[target] = i
            return results
        res = []
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            target = 0 - n
            curr_list = twoSum(nums[i+1:],target)
            for curr in curr_list:
                res.append([n,curr[0], curr[-1]])
        return res