class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1 = Counter(s1)
        c2 = Counter()
        for i in range(len(s2)):
            c2[s2[i]] += 1
            if i >= len(s1):
                leftMost = s2[i - len(s1)]
                if c2[leftMost] == 1:
                    del c2[leftMost]
                else:
                    c2[leftMost] -= 1
            if c1 == c2:
                return True
        return False
