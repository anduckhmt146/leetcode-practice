class Solution:
    def myPow(self, x: float, n: int) -> float:
        def exponent(base, pow):
            # Base case
            if pow == 0:
                return 1.0

            # Divide
            half = exponent(base, pow // 2)

            # Conquer
            if pow % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n

        return exponent(x, n)

