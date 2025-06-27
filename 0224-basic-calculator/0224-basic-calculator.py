class Solution:
    def calculate(self, s: str) -> int:
        def helper(chars: list) -> int:
            stack = []
            num = 0
            sign = '+'  # Start with '+' as default operator

            while chars:
                ch = chars.pop(0)

                if ch.isdigit():
                    num = num * 10 + int(ch)

                if ch == '(':
                    num = helper(chars)  # Evaluate inside parentheses

                # If current char is an operator or end of expression
                if (not ch.isdigit() and ch != ' ') or not chars:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        prev = stack.pop()
                        # Python's int division truncates toward zero
                        stack.append(int(prev / num))
                    sign = ch
                    num = 0

                if ch == ')':
                    break

            return sum(stack)

        return helper(list(s))
