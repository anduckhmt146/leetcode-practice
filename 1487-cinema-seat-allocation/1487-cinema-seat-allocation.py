from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        
        for row, seat in reservedSeats:
            reserved[row].add(seat)
        
        max_families = 0
        
        for row in reserved:
            taken = reserved[row]
            # Check three possible blocks of 4 contiguous seats:
            # Block A: seats 2-5, Block B: seats 4-7, Block C: seats 6-9
            can_place_left = all(seat not in taken for seat in range(2, 6))
            can_place_right = all(seat not in taken for seat in range(6, 10))
            can_place_middle = all(seat not in taken for seat in range(4, 8))

            if can_place_left and can_place_right:
                max_families += 2
            elif can_place_left or can_place_right or can_place_middle:
                max_families += 1
            # Else: no family can be placed in this row

        # Rows without any reserved seats can accommodate 2 families
        rows_without_reservations = n - len(reserved)
        max_families += rows_without_reservations * 2
        
        return max_families
