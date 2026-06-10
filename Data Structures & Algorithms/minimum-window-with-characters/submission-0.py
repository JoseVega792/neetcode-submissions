class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counterT = {}
        for c in t:
            counterT[c] = counterT.get(c, 0) + 1
        
        counterS = {}
        diff = len(counterT)  # distinct chars still needed
        res = ""
        l, r = 0, 0

        while r < len(s):
            c = s[r]
            counterS[c] = counterS.get(c, 0) + 1
            if c in counterT and counterS[c] == counterT[c]:
                diff -= 1
            r += 1

            while diff == 0:
                window = s[l:r]
                if not res or len(window) < len(res):
                    res = window
                lc = s[l]
                counterS[lc] -= 1
                if lc in counterT and counterS[lc] < counterT[lc]:
                    diff += 1
                l += 1

        return res
                



