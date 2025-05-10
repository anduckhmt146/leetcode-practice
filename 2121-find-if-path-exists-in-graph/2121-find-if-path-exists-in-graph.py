class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        result = []

        def dfs(node, target, path = []):
            if node == target:
                result.append(path[:])
                return

            visited[node] = True  # mark as visiting
            path.append(node)
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, target, path)
            
            path.pop()

        dfs(source, destination)
        return len(result) > 0

        