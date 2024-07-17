class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.findUniquePathsRecursive(obstacleGrid, 0, 0, {})

    def findUniquePathsRecursive(self, obstacleGrid, r, c, my_dict):
        if not self.isValid(r, c, len(obstacleGrid), len(obstacleGrid[0])):
            return 0

        if obstacleGrid[r][c] == 1:
            return 0
        
        if r == (len(obstacleGrid) - 1) and c == (len(obstacleGrid[0]) - 1):
            return 1
        
        bottom = 0  
        right = 0
        if (r+1, c) in my_dict:
            bottom = my_dict[(r+1, c)]
        else:
            bottom = self.findUniquePathsRecursive(obstacleGrid, r+1, c, my_dict)
            my_dict[r+1, c] = bottom

        if (r, c+1) in my_dict:
            right = my_dict[(r, c+1)]
        else:
            right = self.findUniquePathsRecursive(obstacleGrid, r, c+1, my_dict)
            my_dict[(r, c+1)] = right

        return bottom + right

    def isValid(self, r, c, m, n):
        if r >= m or c >= n or r < 0 or c < 0:
            return False
        
        return True
