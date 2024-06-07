class Solution:
    def dfs(self, node, graph, path, result, destination):
        if node == destination:
            result.append(list(path))  # Append a copy of the current path
            return
        
        for neighbor in graph[node]:
            path.append(neighbor)  # Explore this neighbor
            self.dfs(neighbor, graph, path, result, destination)
            path.pop()  # Backtrack

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []  # This will store all paths from source to target
        self.dfs(0, graph, [0], result, len(graph)-1)  # Start DFS from node 0 with initial path [0]
        return result