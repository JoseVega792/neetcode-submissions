class Solution:
    def searchList(self, arr: List[int], target:int) -> bool:
        l, r = 0, len(arr) - 1
        while l <= r:
            curr = (l + r) // 2
            if arr[curr] == target:
                return True
            elif arr[curr] < target:
                l = curr + 1
            else:
                r = curr - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            curr = (l + r) // 2
            if matrix[curr][0] == target or matrix[curr][-1] == target:
                return True
            elif matrix[curr][0] > target:
                r = curr - 1
            elif matrix[curr][-1] < target:
                l = curr + 1
            else:
                return self.searchList(matrix[curr], target)
        return False