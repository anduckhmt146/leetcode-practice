from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(a: str, b: str) -> bool:
            # Checks if 'a' is a subsequence of 'b'
            i = 0
            for char in b:
                if i < len(a) and a[i] == char:
                    i += 1
            return i == len(a)

        # Sort by length descending, so we find longest uncommon subsequence first
        strs.sort(key=lambda x: -len(x))

        for i, s in enumerate(strs):
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)
        return -1
