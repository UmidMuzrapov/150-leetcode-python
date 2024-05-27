class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = [ [elem for elem in row] for row in board ]
        m = len(board)
        n = len(board[0])
        cell = 0

        for i in range(0, m):
            for j in range(0, n):
                num_alive = self.getNumAlive(board_copy, i, j, m, n)
                cell = board_copy[i][j]
                if num_alive==2 or num_alive ==3:
                    if cell == 0 and num_alive == 3:
                        board[i][j] = 1
                else:
                    board[i][j] = 0

        
    def getNumAlive(self, board_copy, i, j, m, n):
        directions = {(i+k, j+l) for k in range(-1, 2) for l in range(-1, 2) 
                        if i + k >=0 and j + l>=0 and i + k < m and j+ l <n}
        ones = [i for x, y in directions if board_copy[x][y] == 1] 

        return len(ones) if board_copy[i][j]==0 else len(ones) - 1
