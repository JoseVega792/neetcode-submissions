class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lowerStack = []
        res = [0]* len(temperatures)
        for i,t in enumerate(temperatures):
            while len(lowerStack) > 0 and lowerStack[-1][0] < t:
                lowerVal, ind = lowerStack.pop()
                res[ind] = (i - ind)
            lowerStack.append((t,i))
        return res
