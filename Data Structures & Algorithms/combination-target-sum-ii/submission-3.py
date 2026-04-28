class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, curr, t):
            if not t:
                res.append(curr.copy())
                return
            
            if i == len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, curr, t - candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr.pop()
            backtrack(i + 1, curr, t)
        backtrack(0,[],target)
        return res