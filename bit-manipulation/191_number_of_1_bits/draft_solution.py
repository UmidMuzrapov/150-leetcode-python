class Solution:
    def hammingWeight(self, n: int) -> int:
        hammingWeight = 0

        while n:
            lastBit = (n & 1)
            n >>= 1
            if lastBit: hammingWeight+=1
        
        return hammingWeight
