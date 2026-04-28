class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            curr = str(len(s)) + '#' + s
            res += curr
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                strLen = ''
                while i < len(s) and s[i].isdigit() and s[i] != '#':
                    strLen += s[i]
                    i += 1
                strLen = int(strLen)
                currStr = ""
                i += 1
                while i < len(s) and strLen > 0:
                    currStr += s[i]
                    i += 1
                    strLen -= 1
                res.append(currStr)
            else:
                i += 1
        return res