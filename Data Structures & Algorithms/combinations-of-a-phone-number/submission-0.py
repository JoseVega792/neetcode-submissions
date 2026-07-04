class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, curr):
            if i == len(digits):
                res.append(''.join(curr))
                return 
            
            for c in digitToChar[digits[i]]:
                curr.append(c)
                dfs(i + 1, curr)
                curr.pop()
        dfs(0,[])
        return res
            
