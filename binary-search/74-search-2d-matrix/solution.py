class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        mid = 0
        while bottom!=top:
            mid = (top+bottom)//2
            if matrix[mid][right] > target:
                bottom = mid
            elif matrix[mid][right] < target:
                top = mid + 1
            else:
                return True
    
        while left != right:
            mid = (left+right)//2
            if matrix[top][mid] > target:
                right = mid
            elif matrix[top][mid] < target:
                left = mid + 1
            else:
                return True
        
        return matrix[top][left] == target
