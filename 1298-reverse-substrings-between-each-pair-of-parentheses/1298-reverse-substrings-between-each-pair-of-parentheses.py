from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Initialize a stack for tracking parentheses and their positions
        gstack = deque()
        N = len(s)
        stack = deque()

        i = 0
        while i < N:
            char = s[i]
            
            if char == '(':
                gstack.append(stack)
                stack = deque()
                i += 1

            elif char == ')':
                stack = deque(reversed(stack))
                prev_stack = gstack.pop()
                prev_stack.extend(stack)
                stack = prev_stack
                i += 1

            else:
                stack.append(char)
                i += 1
        
        return ''.join(stack)