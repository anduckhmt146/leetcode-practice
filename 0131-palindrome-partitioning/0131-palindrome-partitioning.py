from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_partition = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int):
            if start == len(s):
                result.append(current_partition[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(end)
                    current_partition.pop()
        
        backtrack(0)
        return result
