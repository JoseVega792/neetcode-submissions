class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                strLen = ''
                while i < len(s) and s[i].isdigit() and s[i] != "#":
                    strLen += s[i]
                    i += 1
                i += 1
                strLen = int(strLen)
                currStr = ""
                while i < len(s) and strLen>0 :
                    currStr += s[i]
                    i += 1
                    strLen -= 1
                res.append(currStr)
            else:
                i += 1
        return res