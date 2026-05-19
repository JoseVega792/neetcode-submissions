class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}':'{', ')':'(', ']':'['}
        remaining = []
        for c in s:
            if c in pairs:
                if len(remaining) > 0 and pairs[c] == remaining[-1]:
                    remaining.pop()
                else:
                    return False
            else:
                remaining.append(c)
        return len(remaining) == 0