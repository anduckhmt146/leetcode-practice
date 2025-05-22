from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers. The result is the XOR of the two unique numbers.
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set (i.e., 1) in xor_all.
        # This bit is different between the two unique numbers.
        diff_bit = xor_all & -xor_all
        
        # Step 3: Divide numbers into two groups and XOR separately.
        result = [0, 0]
        for num in nums:
            if num & diff_bit:
                result[0] ^= num
            else:
                result[1] ^= num
                
        return result
