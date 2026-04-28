class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        res, l = 0, 0
        for r,c in enumerate(s):
            if c in chars:
                l = max(l, chars[c])
            chars[c] = r + 1
            res = max(res, (r - l) + 1)
        return res