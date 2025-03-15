from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def dfs(start_index: int, path: List[str]):
            if start_index == len(s):
                ans.append(path[:])  # Add a copy of the path to the result
                return
            
            for end in range(start_index, len(s)):
                substring = s[start_index:end + 1]
                if is_palindrome(substring):  # Prune invalid paths
                    path.append(substring)
                    dfs(end + 1, path)
                    path.pop()  # Backtrack
        
        dfs(0, [])
        return ans
