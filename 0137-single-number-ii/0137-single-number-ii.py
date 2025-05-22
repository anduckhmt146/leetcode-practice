from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            bit_sum = sum((num >> i) & 1 for num in nums)
            if bit_sum % 3 != 0:
                result |= (1 << i)

        # Handle negative numbers (since Python ints are not limited to 32-bit)
        if result >= 2**31:
            result -= 2**32
        return result
