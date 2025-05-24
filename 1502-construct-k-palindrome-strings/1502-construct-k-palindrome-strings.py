from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False  # Not enough characters to make k palindromes

        char_counts = Counter(s)
        odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)

        return odd_count <= k
