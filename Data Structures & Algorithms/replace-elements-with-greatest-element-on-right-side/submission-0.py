class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = len(arr) - 1
        prevMax = arr[last]
        prevVal = arr[last]
        for i in range(last - 1, -1, -1):
            prevVal = arr[i]
            arr[i] = prevMax
            prevMax = max(prevMax, arr[i], prevVal)
        arr[last] = -1
        return arr
            