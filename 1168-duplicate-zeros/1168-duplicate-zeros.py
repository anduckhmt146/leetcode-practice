from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        
        # Count the number of zeros to be duplicated
        for i in range(n):
            if arr[i] == 0:
                zeros += 1

        # Start from the end and move elements backwards
        i = n - 1
        j = n + zeros - 1

        while i < j:
            if j < n:
                if arr[i] != 0:
                    arr[j] = arr[i]
                else:
                    arr[j] = 0
            j -= 1

            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
            i -= 1
