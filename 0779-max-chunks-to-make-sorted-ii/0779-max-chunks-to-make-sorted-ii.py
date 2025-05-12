from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        max_left = [0] * n
        min_right = [0] * n

        # Fill max_left array
        max_left[0] = arr[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i])

        # Fill min_right array
        min_right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i])

        # Count valid chunks
        chunks = 0
        for i in range(n - 1):
            if max_left[i] <= min_right[i + 1]:
                chunks += 1

        return chunks + 1
