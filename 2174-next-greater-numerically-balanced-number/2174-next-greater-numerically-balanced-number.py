from itertools import permutations

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        digits = ['1', '2', '3', '4', '5', '6']
        best = float('inf')

        for mask in range(1, 1 << 6):  # try all digit subsets
            s = ""
            for i, d in enumerate(digits):
                if (mask >> i) & 1:
                    s += d * int(d)

            # small optimization: if number too small, skip
            if int(''.join(sorted(s))) > best:
                continue

            # Generate permutations lazily
            for p in permutations(sorted(s)):  # sorted gives ascending order
                val = int(''.join(p))
                if val > n:
                    best = min(best, val)
                    break   # stop for this subset once smallest > n is found

        return best
