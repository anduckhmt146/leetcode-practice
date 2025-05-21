class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query: str, pattern: str) -> bool:
            i = 0  # Pointer for pattern
            for c in query:
                if i < len(pattern) and c == pattern[i]:
                    i += 1
                elif c.isupper():
                    return False  # Uppercase letter not in pattern
            return i == len(pattern)  # All of pattern must be matched

        return [match(query, pattern) for query in queries]