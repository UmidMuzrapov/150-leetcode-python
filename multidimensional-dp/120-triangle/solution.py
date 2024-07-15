class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.helper(triangle, 0, 0, {})
        

    def helper(self, triangle, row, col, memo):
        if row >= len(triangle):
            return 0
        
        next_val = memo[(row + 1, col)] if (row + 1, col) in memo else self.helper(triangle, row + 1, col, memo) 
        next_val_right = memo[(row + 1, col+1)] if (row + 1, col+1) in memo else self.helper(triangle, row + 1, col+1, memo)
        memo[(row+1, col)] = next_val
        memo[(row+1, col+1)] = next_val_right

        return triangle[row][col] + min(next_val, next_val_right)
        
