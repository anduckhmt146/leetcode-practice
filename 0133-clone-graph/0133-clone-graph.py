"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # Dictionary to store cloned nodes

        def dfs(current: 'Node') -> 'Node':
            if current in visited:
                return visited[current]

            # Clone the current node
            copy = Node(current.val)
            visited[current] = copy  # Mark as visited (cloned)

            # Visit all neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))  # Recursively clone neighbors

            return copy

        return dfs(node)
        