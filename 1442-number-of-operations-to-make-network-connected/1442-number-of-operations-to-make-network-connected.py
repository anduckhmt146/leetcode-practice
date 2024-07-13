class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if (len(connections) < n - 1):
            return -1
        
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        visited = [False] * n
        num_components = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i, visited)
                num_components += 1
        
        return num_components - 1
        

        