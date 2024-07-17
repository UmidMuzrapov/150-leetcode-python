class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.recursivePathSum(0, 0, grid, {})
    
    def recursivePathSum(self, r, c, grid, memo):
        if not self.isValid(r, c, len(grid), len(grid[0])):
            return 100000

        if r == (len(grid) - 1) and c == (len(grid[0]) - 1):
            return grid[r][c] 

        down = memo[(r+1, c)] if (r+1, c) in memo else self.recursivePathSum(r+1, c, grid, memo)
        right = memo[(r, c+1)] if (r, c+1) in memo else self.recursivePathSum(r, c+1, grid, memo)

        memo[(r+1,c)]= down
        memo[(r, c+1)] =right

        return grid[r][c] + min(down, right)
        
    
    def isValid(self, r, c, m, n):
        if r >= m or c >= n or r < 0 or c < 0:
            return False
        
        return True
