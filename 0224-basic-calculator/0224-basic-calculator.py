class Solution:
    def calculate(self, s: str) -> int:
        def helper(chars):
            num = 0
            sign = '+'
            stack = []
            while chars:
                ch = chars.pop(0)

                if ch.isdigit():
                    num = num * 10 + int(ch)
                
                if ch == '(':
                    num = helper(chars)

                # not digit -> sign or not chars
                if (not ch.isdigit() and ch != ' ') or not chars:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        prev = stack.pop()
                        stack.append(int(prev / num))  # Truncate toward zero

                    sign = ch
                    num = 0

                if ch == ')':
                    break
                
            return sum(stack)

        return helper(list(s))


        