class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        
        s = [1, 2, 2]
        i = 2  # pointer to the index in s that tells us how many times to append
        num = 1  # next number to append (flip between 1 and 2)

        while len(s) < n:
            s.extend([num] * s[i])
            num = 3 - num  # flip between 1 and 2
            i += 1

        return s[:n].count(1)
