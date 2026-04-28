class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        prev = [0] * (len(text1) + 1)
        curr = [0] * (len(text1) + 1)
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1, -1, -1):
                if text2[i] == text1[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
            prev, curr = curr, prev
        return prev[0]

