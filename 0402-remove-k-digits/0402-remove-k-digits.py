class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k > 0, remove the last k digits
        stack = stack[:-k] if k else stack

        # Convert to string and remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"