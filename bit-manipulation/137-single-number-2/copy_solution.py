class Solution:

    def singleNumber(self, nums: list[int]) -> int:

        # `once` tracks bits that have appeared once

        # `twice` tracks bits that have appeared twice

        once = twice = 0

      

        for num in nums:

            # Update `once` and `twice` with current number `num`

            # `once` should only hold bits that are exactly seen once so far

            # And `twice` should only hold bits that are exactly seen twice so far

            # Bits seen three times should be cleared from both `once` and `twice`

          

            # First, calculate `once` considering the current number `num`

            # Use `twice` to mask bits that are already seen two times before

            # because we want to ignore the third time

          

            # The operations can be explained as:

            # If `once` is already set, and current bit of num is 0, keep `once`

            # If `once` is not set, and `twice` and current bit is set, set `once`

            # This updates bit in `once` only if bit in `num` is 1 and wasn't part

            # of `twice`, or if bit in `num` is 0 and bit was already set in `once`.

            once_new = (~once & twice & num) | (once & ~twice & ~num)

          

            # Next, calculate `twice` considering the current number `num`

            # Bits in `once` are used to clear bits that appear for the third time

            # This updates bits in `twice` only if bit in `num` is different from bit in `twice`

            # and bit in `once` is 0, to ensure it's not the third time we see this bit.

            twice_new = ~once & (twice ^ num)

          

            # Update `once` and `twice`

            once, twice = once_new, twice_new

          

        # Return the number that appears only once

        # All bits in `once` have now appeared either 0 or 3 times, which will end up with 0

        # All bits in `twice` have now appeared exactly once or twice, which end up with 0

        # Only the single number will set bits in `twice`

        return twice
