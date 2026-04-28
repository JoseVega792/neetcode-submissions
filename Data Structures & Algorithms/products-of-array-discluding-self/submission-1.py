class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1]
        for i in range(len(nums)-1):
            prev.append(nums[i] * prev[-1])

        post = [1]
        for i in range(len(nums)-1,0,-1):
            post.append(nums[i] * post[-1])
        post = post[::-1]
        
        res = []
        for i in range(len(nums)):
            res.append(prev[i] * post[i])
        return res

