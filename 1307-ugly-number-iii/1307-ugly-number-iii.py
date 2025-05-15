from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # Least Common Multiple
        def lcm(x, y):
            return x * y // gcd(x, y)

        # Count of numbers <= x divisible by a, b, or c
        def count(x):
            ab = lcm(a, b)
            bc = lcm(b, c)
            ac = lcm(a, c)
            abc = lcm(ab, c)
            return (x // a) + (x // b) + (x // c) - (x // ab) - (x // bc) - (x // ac) + (x // abc)

        # Binary search to find the smallest number with count >= n
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left
