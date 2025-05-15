class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Count how many numbers in the m x n multiplication table are less than or equal to x.
        def count(x):
            total = 0
            for i in range(1, m + 1):
                total += min(x // i, n)
            return total
        
        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

        