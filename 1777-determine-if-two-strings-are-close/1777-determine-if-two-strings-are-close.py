from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Must be same length
        if len(word1) != len(word2):
            return False

        # Same characters
        if set(word1) != set(word2):
            return False

        # Same frequency pattern (ignoring which character)
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
        