class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        
        for c in s:
            if c in tCount:
                if sCount[c] != tCount[c]:
                    return False
            else:
                return False
        
        for c in t:
            if c in sCount:
                if sCount[c] != tCount[c]:
                    return False
            else:
                return False
        return True
        