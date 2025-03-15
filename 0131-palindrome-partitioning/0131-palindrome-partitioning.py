from typing import List

# We start at index 0 and try to partition the string at different points.
# If a substring is a palindrome, we add it to our current partition (path) and recur for the remaining string.
# Once we reach the end of the string, we store the valid partition.
# We then backtrack (undo the last addition) to explore other possibilities.

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
