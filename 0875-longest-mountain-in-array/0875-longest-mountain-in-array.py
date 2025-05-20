from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        i = 1  # Start from second element

        while i < n - 1:
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Expand left
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                # Expand right
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                # Update longest mountain
                longest = max(longest, right - left + 1)
                i = right  # Move i to the end of this mountain
            else:
                i += 1  # Not a peak, move forward

        return longest
