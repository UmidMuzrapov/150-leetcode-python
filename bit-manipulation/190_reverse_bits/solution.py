class Solution:
    def reverse_bits(self, n: int) -> int:
        """
        Reverse the bits of a given 32-bit unsigned integer.

        Args:
            n (int): A 32-bit unsigned integer.

        Returns:
            int: The integer with reversed bits.
        """
        INT_SIZE = 32
        reversed_num = 0

        for i in range(INT_SIZE):
            # Extract the least significant bit of n
            bit = n & 1
            # Shift the extracted bit to its new position
            shifted_bit = bit << (INT_SIZE - 1 - i)
            # Add the shifted bit to the result
            reversed_num |= shifted_bit
            # Right shift n to process the next bit
            n >>= 1

        return reversed_num
