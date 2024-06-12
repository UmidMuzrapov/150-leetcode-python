class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n*n
        snake = {}

        for r in range(n):
            for c in range(n):
                if board[n-r-1][c] != -1:
                    if r%2 == 0:
                        snake[n*r+c+1] = board[n-r-1][c]
                    else:
                        snake[n*(r+1)-c] = board[n-r-1][c]

        
        if len(snake) == 0:
            return target//6 + (0 if target%6==0 else 1)

        level = [1]
        step = 0
        marked = [False for _ in range(target+1)]
        while len(level) > 0:
            next_level = []
            for u in level:
                marked[u] = True
                if u == target:
                    return step      
                else:
                    for v in range(u+1, min(u+7, target+1)):
                        if v in snake:
                            if not marked[snake[v]]:
                                next_level.append(snake[v])
                        elif not marked[v]:
                                next_level.append(v)
                    
            level = next_level
            step+=1

        return -1
                
