class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        splitted = s.split()
        return ' '.join(splitted[::-1])
