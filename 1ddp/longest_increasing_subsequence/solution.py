class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(nums, 0, -1, {})
    
    def helper(self, nums, start, prev_index, memo):
        if start >= len(nums):
            return 0

        if start in memo:
            return memo[start]

        longest_sequence = 0
        for i in range(start, len(nums)):
            if prev_index == -1 or nums[i] > nums[prev_index]:
                larger_than_num = self.helper(nums, i + 1, i, memo) + 1
                longest_sequence = max(longest_sequence, larger_than_num)

        memo[start] = longest_sequence
        return longest_sequence
