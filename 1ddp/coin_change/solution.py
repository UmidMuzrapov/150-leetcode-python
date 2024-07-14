class Solution:
    '''
        Get the fewest number of coins that add up to amount.
        If the amount cannot be made up, return -1.
        If the amount is zero, return 0.
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dfs(coins, amount, {})

    def dfs(self, coins, amount, memo):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        else:
            if amount in memo:
                return memo[amount]
            
            memo[amount] = 2**31

            for coin in coins:
                additional_coins = self.dfs(coins, amount - coin, memo)
                if additional_coins >= 0 and memo[amount] > additional_coins + 1:
                    memo[amount] = additional_coins + 1

            return memo[amount] if memo[amount] < 2**31 else -1
        

