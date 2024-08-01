class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        INT_SIZE = 32

        for i in range(INT_SIZE):
            reverse |= (n & 1) << (INT_SIZE - 1 - i)
            n >>= 1
        
        return reverse
