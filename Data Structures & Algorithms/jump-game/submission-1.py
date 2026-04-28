class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        r = 0
        l = 0
        while l < r or (l == r and nums[l] != 0):
            r = max(r, l + nums[l])
            if r >= len(nums) - 1:
                return True
            l += 1
        return r >= len(nums) - 1