class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2

        # Step 1: Find the first decreasing digit from the right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i == -1:
            return -1  # digits are in descending order, no next permutation

        # Step 2: Find the next greater digit to the right of digits[i]
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: Swap and reverse the suffix
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])

        # Step 4: Convert back to integer
        result = int("".join(digits))

        # Step 5: Check if result is within 32-bit signed integer range
        return result if result < 2**31 else -1
