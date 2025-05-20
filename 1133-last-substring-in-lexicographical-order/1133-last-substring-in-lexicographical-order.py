class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = max(s)
        candidates = [i for i, c in enumerate(s) if c == max_char]
        return max(s[i:] for i in candidates)
        