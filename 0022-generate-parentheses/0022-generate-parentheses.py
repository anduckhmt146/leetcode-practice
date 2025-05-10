from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if the current string has all pairs
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an opening parenthesis if we still have one
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a closing parenthesis if it won't exceed the number of opens
            
            # Why You Don’t See current.pop()
            # That creates a new string every time (current + "("), so we don’t need to undo        anything — the old current is untouched.
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result
