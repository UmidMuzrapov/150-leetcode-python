class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the single number in a list where every element appears twice except for one.
        
        Args:
            nums (List[int]): A list of integers where every element appears twice except for one.
        
        Returns:
            int: The single number that appears only once.
        
        Time complexity: O(n), where n is the length of the input list.
        Space complexity: O(1), constant extra space is used.
        """
        result = 0
        for num in nums:
            result ^= num
        return result
