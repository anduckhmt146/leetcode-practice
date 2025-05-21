from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(word: str):
            groups = []
            count = 1
            for i in range(1, len(word)):
                if word[i] == word[i-1]:
                    count += 1
                else:
                    groups.append((word[i-1], count))
                    count = 1
            groups.append((word[-1], count))
            return groups

        s_groups = get_groups(s)
        result = 0

        for word in words:
            w_groups = get_groups(word)
            if len(w_groups) != len(s_groups):
                continue
            match = True
            for (sc, scount), (wc, wcount) in zip(s_groups, w_groups):
                if sc != wc:
                    match = False
                    break
                if scount < 3:
                    if scount != wcount:
                        match = False
                        break
                else:
                    if wcount > scount or wcount < 1:
                        match = False
                        break
            if match:
                result += 1

        return result
