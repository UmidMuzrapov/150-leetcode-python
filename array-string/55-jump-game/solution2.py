class Solution:
    """
        We will use greedy approach.
        Set max_reach to nums[0]
        iterate over the array, update max_reach (max of max_reach, i + nums[i])
            check i > max_reach -> you cannot reach the index. return false
            max_reach >= len(nums) - 1 -> you can reach the end. return true
        
        If we have iterated over all elements without any problem, we can reach the end. reutrn true.

        

    """
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        max_reach = 0

        for i in range(n):
            if i > max_reach:
                return False

            if max_reach >= n - 1:
                return True

            max_reach = max_reach if max_reach >= i + nums[i] else i + nums[i]

        return True
            
