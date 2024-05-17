class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        buy = True
        max_profit = 0
        purchase_price = 0
        length = len(prices)
        index = 0

        while index < length:
            price = prices[index]

            if buy:
                if index == length - 1:
                    break
                
                next_price = prices[index+1]
                if next_price > price:
                    purchase_price = price
                    buy = False

            else:
                if price > purchase_price:
                    local_max_i = local_max(prices, index)
                    max_profit += (prices[local_max_i] - purchase_price)
                    index = local_max_i
                    buy = True

            index+=1

        return max_profit
            
def local_max(prices, start):

    for i in range(start, len(prices) - 1):
        next_price = prices[i+1]
        if next_price < prices[i]:
            return i
        
    return len(prices) - 1
