class Solution:
    '''
        input: target, nums
        output: minimal length of a subarray whose sum is greater than or equal to target
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        my_sum = 0
        start = 0
        n = len(nums)
        min_sub = 10**6

        for i in range(n):
            my_sum+=nums[i]
            while my_sum >= target and start < n:
                min_sub = min(min_sub, i - start + 1)
                my_sum -= nums[start]
                start += 1
                

        return min_sub if min_sub <= 10**5 else 0

