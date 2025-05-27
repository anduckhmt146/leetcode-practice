class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_not_divisible = sum(i for i in range(1, n + 1) if i % m != 0)
        sum_divisible = sum(i for i in range(1, n + 1) if i % m == 0)
        return sum_not_divisible - sum_divisible
