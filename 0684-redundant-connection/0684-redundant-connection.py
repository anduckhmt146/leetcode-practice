from typing import List

class Solution:
    # \U0001f9e0 Step-by-step Processing
    # 1. Edge: [1, 2]
    # find(1) = 1, find(2) = 2 → different groups → no cycle

    # union(1, 2) → make parent[2] = 1

    # Now: parent = [0, 1, 1, 3, 4, 5]

    # 2. Edge: [2, 3]
    # find(2):

    # parent[2] = 1, so find(1) = 1 → find(2) = 1

    # find(3) = 3

    # Different groups → no cycle

    # union(2, 3) → make parent[3] = 1

    # Now: parent = [0, 1, 1, 1, 4, 5]

    # 3. Edge: [3, 4]
    # find(3):

    # parent[3] = 1 → find(3) = 1

    # find(4) = 4

    # Different groups → no cycle

    # union(3, 4) → make parent[4] = 1

    # Now: parent = [0, 1, 1, 1, 1, 5]

    # 4. Edge: [1, 4]
    # find(1) = 1

    # find(4):

    # parent[4] = 1 → find(4) = 1

    # Same root → cycle detected!
    # ✅ This edge is redundant → return [1, 4]

    # 5. (Optional) Edge: [1, 5]
    # We already returned [1, 4], so we stop before processing this.
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX
            return True

        for u, v in edges:
            if not union(u, v):
                print(parent)
                return [u, v]
