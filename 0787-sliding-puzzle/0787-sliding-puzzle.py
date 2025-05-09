from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(cell) for row in board for cell in row)
        target = '123450'

        # Mapping of index to its neighbors on a 2x3 board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps

            zero_idx = state.index('0')
            for neighbor in neighbors[zero_idx]:
                new_state = list(state)
                # Swap '0' with the neighbor
                new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, steps + 1))

        return -1
