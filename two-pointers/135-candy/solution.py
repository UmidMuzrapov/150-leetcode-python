class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]
        n = len(ratings)

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
            
        return sum(candies)
