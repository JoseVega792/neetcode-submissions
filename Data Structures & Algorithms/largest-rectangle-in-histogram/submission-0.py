class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i,n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                ind, h = stack.pop()
                maxCalc = max(h, h * (i - ind))
                res = max(res, maxCalc)
                start = ind
            stack.append((start,n))

        while stack:
                ind, h = stack.pop()
                maxCalc = max(h, h * ((len(heights) - ind)))
                res = max(res, maxCalc)
        return res