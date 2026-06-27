class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(openCount, closedCount):
            if openCount == closedCount == n:
                res.append(''.join(stack))
                return
            if openCount < n:
                stack.append('(')
                dfs(openCount + 1, closedCount)
                stack.pop()
            if closedCount < openCount:
                stack.append(')')
                dfs(openCount, closedCount + 1)
                stack.pop()
        dfs(0,0)
        return res