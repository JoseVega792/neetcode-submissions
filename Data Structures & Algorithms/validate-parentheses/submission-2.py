class Solution:
    def isValid(self, s: str) -> bool:
        contains = {')':'(', '}':'{',']':'['}
        stack = []
        for c in s:
            if c in contains and stack and stack[-1] == contains[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0