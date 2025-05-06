class Solution:
    def removeStones(self, stones):
        parent = {}

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            row = f"r{x}"
            col = f"c{y}"
            union(row, col)

        unique_groups = {find(x) for x in parent}
        return len(stones) - len(unique_groups)
