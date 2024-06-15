class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [num for num in range(1, n+1)]
        self.helper(0, k, nums, [], result)
        return result

        
    def helper(self, start, k, nums, accum, result):
        if start == k:
            result.append([num for num in accum])

        size = len(nums)
        for i in range(size):
            accum.append(nums[i])
            self.helper(start+1, k, nums[i+1:], accum, result)
            accum.pop()

