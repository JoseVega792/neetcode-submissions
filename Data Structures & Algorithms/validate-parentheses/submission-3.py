class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ')':'(', ']':'['}
        for c in s:
            if c in pairs:
                if len(stack) > 0 and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0