from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for num in arr1:
            # Binary search to find the insertion point in arr2
            index = bisect.bisect_left(arr2, num)

            # Check left neighbor and right neighbor (if any)
            left_close = abs(num - arr2[index - 1]) if index > 0 else float('inf')
            right_close = abs(num - arr2[index]) if index < len(arr2) else float('inf')

            # If both neighbors are farther than d, count this number
            if min(left_close, right_close) > d:
                count += 1

        return count
