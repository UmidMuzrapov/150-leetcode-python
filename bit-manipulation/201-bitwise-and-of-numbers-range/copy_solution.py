class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Compute the bitwise AND of all numbers in the range [left, right].

        This method uses the concept of finding the common prefix in the binary
        representations of left and right boundaries.

        Args:
            left (int): The lower bound of the range, inclusive.
            right (int): The upper bound of the range, inclusive.

        Returns:
            int: The bitwise AND of all numbers in the range [left, right].

        Time complexity: O(log(max(left, right)))
        Space complexity: O(1)
        """
        shift_count = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift_count += 1

        return left << shift_count
