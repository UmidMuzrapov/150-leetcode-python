class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        i = 0

        while True:
            if i + nums[i] >= n - 1:
                return jumps if n == 1 else jumps + 1

            i = best_jump(nums, i)
            jumps += 1
                 

def best_jump(nums, start):
    max_reach = start + nums[start]
    max_index = start

    for i in range(start, start + nums[start] + 1):
        jump = i + nums[i]
        if jump > max_reach:
            max_reach = jump 
            max_index = i
    
    return max_index
        

