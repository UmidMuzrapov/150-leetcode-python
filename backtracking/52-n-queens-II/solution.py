class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row):
            if row == n:
                nonlocal result
                result+=1
                return 

            for col in range(n):
                pos_dig = row + col
                pos_adig = row - col +n
                if cols[col] or dig[pos_dig] or adig[pos_adig]:
                    continue
                
                cols[col] = dig[pos_dig] = adig[pos_adig] = True
                dfs(row+1)
                cols[col] = dig[pos_dig] = adig[pos_adig] = False
            
        cols = [False]*n
        dig = [False]*(2*n)
        adig = [False]*(2*n)   
        result = 0
        dfs(0)

        return result
