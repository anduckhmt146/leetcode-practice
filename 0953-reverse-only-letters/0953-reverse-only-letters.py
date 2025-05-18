class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)  # Convert string to list for in-place modification
        left, right = 0, len(s) - 1

        while left < right:
            # Move left to the next vowel
            while left < right and not s[left].isalpha():
                left += 1
            # Move right to the previous vowel
            while left < right and not s[right].isalpha():
                right -= 1
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
        