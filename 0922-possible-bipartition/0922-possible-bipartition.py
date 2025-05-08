class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}

        for node in range(1, n+1):
            if node not in color:
                queue = deque([node])
                color[node] = 0
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[curr]
                            queue.append(neighbor)
                        elif color[neighbor] == color[curr]:
                            return False
        return True
            