class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        prev = [1]
        for n in nums:
            prev.append(prev[-1] * n)
        post = [1]
        for i in range(len(nums)-1,0,-1):
            post.append(post[-1] * nums[i])
        post = post[::-1]
        for i in range(len(nums)):
            res.append(post[i] * prev[i])
        print(post, prev)
        return res
