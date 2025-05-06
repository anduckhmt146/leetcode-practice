class Solution:
    def removeStones(self, stones):
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x  # Initialize parent if x is new

            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression

            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            row = f"r{x}"
            col = f"c{y}"
            union(row, col)

        # {'c0': 'c1', 'r0': 'c0', 'c1': 'c2', 'r1': 'c1', 'c2': 'c2', 'r2': 'c2'}
        print(parent)
        unique_groups = {find(x) for x in parent}

        # {'c2'}
        # For every node in parent, we find its ultimate root using find(x. Then collect all unique roots
        print(unique_groups)
        return len(stones) - len(unique_groups)
