class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        digits = [int(ch) for ch in s]

        def comb_mod10(n, k):
            # compute C(n, k) % 10 iteratively (no factorial)
            res = 1
            for i in range(1, k + 1):
                res = res * (n - i + 1) // i
            return res % 10

        num1 = num2 = 0
        for i in range(n - 1):
            c = comb_mod10(n - 2, i)
            num1 = (num1 + c * digits[i]) % 10
            num2 = (num2 + c * digits[i + 1]) % 10

        return num1 == num2
        