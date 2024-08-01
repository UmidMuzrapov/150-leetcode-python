class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculate the Hamming weight (number of '1' bits) in an integer.

        Args:
            n (int): An unsigned integer.

        Returns:
            int: The Hamming weight of the input integer.
        """
        bit_count = 0

        while n:
            bit_count += n & 1
            n >>= 1

        return bit_count
