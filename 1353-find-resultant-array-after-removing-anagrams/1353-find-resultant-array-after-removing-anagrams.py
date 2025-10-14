class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def encode(word):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            return tuple(freq)

        res = [words[0]]
        prev = encode(words[0])

        for i in range(1, len(words)):
            cur = encode(words[i])
            if cur != prev:
                res.append(words[i])
                prev = cur

        return res

        