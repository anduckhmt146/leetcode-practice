class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {character: index for index, character in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j = 0

            while j < len(w1):
                if j == len(w2):
                    return False

                if orderDict[w1[j]] > orderDict[w2[j]]:
                    return False
                # True
                if w1[j] != w2[j]:
                    break
                j += 1
            
        return True

