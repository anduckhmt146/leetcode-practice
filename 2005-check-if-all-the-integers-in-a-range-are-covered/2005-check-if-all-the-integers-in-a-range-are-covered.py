from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52  # We use size 52 because 1 ≤ left, right ≤ 50

        # Mark the difference array for each range
        for start, end in ranges:
            diff[start] += 1
            if end + 1 <= 51:
                diff[end + 1] -= 1

        # Convert to prefix sum to get actual coverage
        for i in range(1, 52):
            diff[i] += diff[i - 1]

        # Check if all numbers in [left, right] are covered
        for i in range(left, right + 1):
            if diff[i] <= 0:
                return False

        return True
