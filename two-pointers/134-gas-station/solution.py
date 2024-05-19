class Solution:
    '''
        cost of travel from i to i + 1 is cost[i]
        return index of the starting gay station to make a clockwise circle. -1 otherwise.
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
                
        return -1 if total_surplus < 0 else start
