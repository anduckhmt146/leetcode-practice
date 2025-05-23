from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        # Step 1: Find the first index i such that arr[i] > arr[i + 1] from the right
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        
        if i < 0:
            return arr  # Already the smallest permutation
        
        # Step 2: Find the largest j > i such that arr[j] < arr[i]
        # and arr[j] is the rightmost occurrence of that value
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        
        # Move to the leftmost j that has the same value (to avoid unnecessary swaps)
        while j - 1 > i and arr[j] == arr[j - 1]:
            j -= 1
        
        # Step 3: Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]
        
        return arr
