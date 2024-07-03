class Solution:
    '''
        What is the unknown? final maximized capital
        What is data? initial capital w, profits, capital,  k projects
        what are the conditions? at most k projects.
        Pure profit of a chosen project is added to w.
        fits 32-bit 
    '''
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap_by_capital = [(capital[i], profits[i]) for i in range(len(profits))]
        heapify(min_heap_by_capital)
        max_heap_by_profit = []

        while k:
            while min_heap_by_capital and min_heap_by_capital[0][0] <= w:
                heappush(max_heap_by_profit, -heappop(min_heap_by_capital)[1])

            if not max_heap_by_profit:
                break

            w -= heappop(max_heap_by_profit)
            k -= 1

        return w

