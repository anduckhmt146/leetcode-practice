class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0
        for i in range(len(s)):
            # Odd-length palindromes
            total += expand_around_center(i, i)
            # Even-length palindromes
            total += expand_around_center(i, i + 1)

        return total
