from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str, s: str) -> bool:
            # Check if word is a subsequence of s
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            return i == len(word)
        
        longest = ""
        for word in dictionary:
            if is_subsequence(word, s):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest
