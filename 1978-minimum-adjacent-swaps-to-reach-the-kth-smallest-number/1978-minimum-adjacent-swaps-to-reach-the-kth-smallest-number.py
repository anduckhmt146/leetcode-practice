class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
        
        # Step 1: Compute the k-th permutation
        target = list(num)
        for _ in range(k):
            next_permutation(target)
        
        # Step 2: Count minimum adjacent swaps to match target
        original = list(num)
        swaps = 0
        
        for i in range(len(original)):
            if original[i] == target[i]:
                continue
            j = i
            while original[j] != target[i]:
                j += 1
            # Now swap original[j] leftward to position i
            while j > i:
                original[j], original[j - 1] = original[j - 1], original[j]
                swaps += 1
                j -= 1

        return swaps
