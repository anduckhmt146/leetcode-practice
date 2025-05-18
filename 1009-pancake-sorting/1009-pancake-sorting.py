from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            # Order from max 4,3,2,1
            # Find the index of the max number in arr[0:size]
            max_idx = arr.index(max(arr[:size]))
            
            if max_idx == size - 1:
                continue  # Already in correct position
            
            # Flip to bring the max element to the front (if not already there)
            if max_idx != 0:
                res.append(max_idx + 1)
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            
            # Flip to move it to its correct position
            res.append(size)
            arr[:size] = reversed(arr[:size])
        
        return res
