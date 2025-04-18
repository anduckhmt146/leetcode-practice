class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Find the longest non-decreasing prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
            
        # If the entire array is non-decreasing
        if left == n - 1:
            return 0
            
        # Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
            
        # We have two options:
        # 1. Remove everything after left
        # 2. Remove everything before right
        result = min(n - left - 1, right)
        
        # Try to merge the prefix and suffix
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # We can merge from i to j
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
                
        return result
        