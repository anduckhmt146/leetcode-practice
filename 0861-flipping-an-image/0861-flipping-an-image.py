from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Flip the row (reverse it) and invert each value (1 becomes 0, 0 becomes 1)
            for i in range((len(row) + 1) // 2):
                # Swap and invert in a single step
                row[i], row[-i - 1] = 1 - row[-i - 1], 1 - row[i]
        return image