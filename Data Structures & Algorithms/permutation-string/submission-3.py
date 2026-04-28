class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        size = len(s1) - 1
        countS1, countS2 = Counter(s1), Counter(s2[:size])
        for r,c in enumerate(s2[size:]):
            countS2[c] = countS2.get(c,0) + 1
            if countS1 == countS2:
                return True
            countS2[s2[l]] -= 1
            l += 1

        return False
