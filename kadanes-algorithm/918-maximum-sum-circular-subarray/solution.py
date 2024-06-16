class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = cur_min = 0
        global_max = -10**5
        global_min = 10**5
        
        for num in nums:
            cur_max += num
            cur_min += num

            if cur_max > global_max:
                global_max = cur_max

            if cur_min < global_min:
                global_min = cur_min

            if cur_max < 0:
                cur_max = 0
            
            if cur_min > 0:
                cur_min = 0
            
        nums_sum = sum(nums)

        if len(list(filter(lambda x: x < 0, nums))) == len(nums):
            return global_max
        
        return max(global_max, nums_sum - global_min)
            
