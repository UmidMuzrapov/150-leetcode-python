class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        number_rows = len(matrix)
        number_cols = len(matrix[0])
        dp = [[0] * number_cols for _ in range(number_rows)]
        max_side = 0

        for r in range(number_rows):
            for c in range(number_cols):
                if matrix[r][c] == '1':
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    max_side = max(max_side, dp[r][c])
        
        return max_side * max_side

