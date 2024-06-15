class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(0, len(nums), {num for num in nums}, [], result)
        return result
        
    def helper(self, start, target, s, accum, result):
        if start == target:
            result.append([num for num in accum])

        for num in s:
            accum.append(num)
            self.helper(start+1, target, {elem for elem in s if elem != num}, accum, result)
            accum.pop()
