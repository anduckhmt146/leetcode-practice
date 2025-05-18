from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        
        # List of all indices where c appears
        positions = [i for i, char in enumerate(s) if char == c]
        
        # Pointer for positions
        j = 0
        
        for i in range(n):
            # Move j if next c position is closer
            while j < len(positions) - 1 and abs(positions[j + 1] - i) < abs(positions[j] - i):
                j += 1
            result[i] = abs(positions[j] - i)
        
        return result
