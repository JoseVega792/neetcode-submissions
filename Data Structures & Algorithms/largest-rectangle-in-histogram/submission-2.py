class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                j, h = stack.pop()
                currMax = max(h, h * (i - j))
                res = max(res, currMax)
                start = j
            stack.append((start, n))
        
        while stack:
            i, h = stack.pop()
            res = max(res, h, h * (len(heights) - i))
        return res