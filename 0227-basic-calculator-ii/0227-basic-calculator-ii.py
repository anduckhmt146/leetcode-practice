class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'  # Initially assume the number is positive
        s = s.replace(" ", "")  # Remove spaces for easier parsing

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # truncate toward zero
                # ch = '*': previous sign = '+' → push 2 → stack = [3, 2], update sign = '*'
                sign = ch
                num = 0

        return sum(stack)
