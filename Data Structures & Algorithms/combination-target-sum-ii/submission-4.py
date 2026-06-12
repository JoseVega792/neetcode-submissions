class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,curr, arr):
            if curr == target:
                res.append(arr.copy())
                return
            if i >= len(candidates) or curr > target:
                return
            
            #Keep
            curr += candidates[i]
            arr.append(candidates[i])
            dfs(i + 1, curr, arr)
            #Dont
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr -= candidates[i]
            arr.pop()
            dfs(i + 1, curr, arr)
        dfs(0,0,[])
        return res