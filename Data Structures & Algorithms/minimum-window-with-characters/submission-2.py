class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counterT = Counter(t)
        counterS = {}
        diff = len(counterT)
        res = ""
        l, r = 0, 0
        while r < len(s):
            rChar = s[r]
            counterS[rChar] = counterS.get(rChar,0) + 1
            if rChar in counterT and counterS[rChar] == counterT[rChar]:
                diff -= 1
            r += 1
            while diff == 0:
                window = s[l:r]
                if not res or len(res) > len(window):
                    res = window
                lChar = s[l]
                counterS[lChar] -= 1
                if lChar in counterT and counterS[lChar] < counterT[lChar]:
                    diff += 1
                l += 1
        return res