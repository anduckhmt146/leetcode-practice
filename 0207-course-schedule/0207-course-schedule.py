from collections import defaultdict, deque
from typing import List

# BFS Topology Sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Initialize queue with nodes having zero in-degree (no prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0

        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            completed_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        print("Result: ", result)
        return completed_courses == numCourses
