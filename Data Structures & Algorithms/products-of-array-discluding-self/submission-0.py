class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first = []
        sec = []

        temp = 1
        for n in nums:
            temp *= n
            first.append(temp)
        
        temp = 1
        for n in range(len(nums)-1,-1,-1):
            temp *= nums[n]
            sec.append(temp)
        
        sec = sec[::-1]

        res = []
        for i in range(len(first)):
            prev = first[i-1] if i - 1 >= 0 else 1
            after = sec[i + 1] if i + 1 < len(first) else 1
            res.append(prev * after)
        return res