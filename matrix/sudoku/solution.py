class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_set = set()
        n = len(board)

        for row in board:
            for elem in row:
                if elem in my_set and elem != ".":
                    return False
                my_set.add(elem)
            my_set.clear()
    
        elem = 0
        
        for col in range(n):
            for row in range(n):
                elem = board[row][col]
                if elem in my_set and elem != ".":
                    return False
                
                my_set.add(elem)

            my_set.clear()

        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                for row_i in range(row, row+3):
                    for col_i in range(col, col+3):
                        elem = board[row_i][col_i]
                        if elem in my_set and elem != ".":
                            return False
                        my_set.add(elem)
                my_set.clear()

        return True

