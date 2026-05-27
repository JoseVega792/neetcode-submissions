class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        seen = set()
        while l < len(s) and r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            currLen = r - l
            res = max(res, currLen)
            seen.remove(s[l])
            l += 1
        return res
            
            