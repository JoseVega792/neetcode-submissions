class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i,n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                j,h = stack.pop()
                maxArea = max(h,h * (i - j))
                res = max(res, maxArea)
                start = j
            stack.append((start,n))
        
        while stack:
            i,h = stack.pop()
            maxArea = max(h, h * (len(heights) - i))
            res = max(res, maxArea)
        return res