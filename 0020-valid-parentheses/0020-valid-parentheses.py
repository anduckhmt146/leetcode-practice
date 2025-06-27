class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                top = stack.pop()
                if char != mapping[top]:
                    return False

        return not stack
                
        