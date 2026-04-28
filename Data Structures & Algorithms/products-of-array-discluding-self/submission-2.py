class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        pref = [1]
        for n in nums:
            pref.append(pref[-1] * n)
        post = [1]
        for i in range(len(nums) - 1, 0, -1):
            post.append(post[-1] * nums[i])
        post = post[::-1]
        print(post)
        for i in range(len(nums)):
            prevVal = pref[i]
            postVal = post[i]
            res.append(prevVal * postVal)
        return res
