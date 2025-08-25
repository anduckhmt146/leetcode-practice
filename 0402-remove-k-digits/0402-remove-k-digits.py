class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            # Push to stack
            # If số sau < số trước => Push vào stack
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1

            stack.append(c)

        while stack and k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')
        return res if res else '0'        