class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array):
            l = 0
            r = len(array) - 1
            while l <= r:
                mid = (r + l) // 2
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        ind = len(matrix) - 1
        for i in range(len(matrix) - 1, -1, -1):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] < target:
                return binarySearch(matrix[i])
        return False