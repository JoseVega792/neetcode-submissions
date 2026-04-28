class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array):
            l = 0
            r = len(array) - 1
            while l <= r:
                mid = (l + r) // 2
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        for r in range(len(matrix)-1 ,-1 ,-1):
            if matrix[r][0] == target:
                return True
            
            if matrix[r][0] < target:
                return binarySearch(matrix[r])
        return False