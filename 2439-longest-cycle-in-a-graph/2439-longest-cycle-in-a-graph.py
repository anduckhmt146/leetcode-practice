from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        state = [0] * len(edges)  # 0 = unvisited, 1 = visiting, 2 = safe
        max_cycle_length = -1
        
        def dfs(node, path):
            if state[node] == 1:  # cycle detected
                cycle_start = node
                cycle_length = 0
                for i in range(len(path) - 1, -1, -1):
                    cycle_length += 1
                    if path[i] == cycle_start:
                        break
                return cycle_length

            if state[node] == 2:  # already safe
                return 0
            
            state[node] = 1  # mark as visiting
            
            path.append(node)
            next_node = edges[node]
            
            cycle_length = 0
            # Loop dfs from a node until meet cycle
            if next_node != -1:  # valid edge
                cycle_length = dfs(next_node, path)

            state[node] = 2  # mark as safe
            path.pop()
            
            return cycle_length
        
        for i in range(len(edges)):
            if state[i] == 0:  # unvisited node
                cycle_length = dfs(i, [])
                max_cycle_length = max(max_cycle_length, cycle_length)
        
        return max_cycle_length if max_cycle_length > 0 else -1
