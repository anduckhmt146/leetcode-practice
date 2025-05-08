from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        out_degree = [0] * (n + 1)
        in_degree = [0] * (n + 1)

        for a, b in trust:
            graph[a].append(b)
            out_degree[a] += 1
            in_degree[b] += 1

        # def dfs(person, visited):
        #     visited.add(person)
        #     for neighbor in graph[person]:
        #         if neighbor not in visited:
        #             dfs(neighbor, visited)

        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i

        return -1
