from typing import List

class UnionFind:
    def __init__(self, n):
        # Initialize parent to itself, rank to 0
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            # Path compression: flatten the structure for faster future queries
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank: attach the smaller tree under the larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # If there are fewer than n-1 connections, we can't connect all nodes
        if len(connections) < n - 1:
            return -1
        
        # Initialize Union-Find structure
        uf = UnionFind(n)
        
        # Process all the connections and unite the nodes
        for u, v in connections:
            uf.union(u, v)
        
        # Count the number of connected components
        components = 0
        for i in range(n):
            if uf.find(i) == i:  # If a node is its own parent, it's a root (a separate component)
                components += 1
        
        # The number of operations needed is the number of components minus 1
        return components - 1
