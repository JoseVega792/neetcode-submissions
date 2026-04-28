class Solution:
    def binarySearch(self, row, target):
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (r + l) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix) - 1, -1, -1):
            if matrix[r][0] == target:
                return True
            
            if matrix[r][0] < target:
                return self.binarySearch(matrix[r], target)

        return False