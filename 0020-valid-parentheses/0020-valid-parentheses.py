class Solution:
    def isValid(self, s: str):
        # Your code goes here
        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if char != mapping[top]:
                    return False
        
        return not stack