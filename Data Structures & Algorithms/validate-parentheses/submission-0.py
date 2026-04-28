class Solution:
    def isValid(self, s: str) -> bool:
        prev = []
        seen = {')':'(','}':'{',']':'['}
        for c in s:
            if c in seen:
                if len(prev) > 0 and prev[-1] == seen[c]:
                    prev.pop()
                else:
                    return False
            else:
                prev.append(c)
        return len(prev) == 0