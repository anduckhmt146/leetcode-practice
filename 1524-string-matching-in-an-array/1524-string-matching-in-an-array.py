class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # O(NlogN)
        # O(N^2)
        # Remove dup
        result = set()
        sortedWords = sorted(words, key=len)
        for i in range(0, len(sortedWords) - 1):
            for j in range(i + 1, len(sortedWords)):
                if sortedWords[i] in sortedWords[j]:
                    result.add(sortedWords[i])

        return list(result)

        