class Solution:
    '''
        Use left and right pointer. 
        leftp
        rightp
        if left >= right
           leftp = rightp
        else:
            if (right - left) > max:
                go
    '''
    def maxProfit(self, prices: List[int]) -> int:
        left_p = 0
        right_p = 1
        max_val = 0
        
        while right_p < len(prices):
            if prices[left_p] >= prices[right_p]:
                left_p = right_p
            else:
                profit = prices[right_p] - prices[left_p] 
                if profit > max_val:
                    max_val = profit

            right_p+=1
