class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Still run 0 -> n
        n = len(graph)
        state = [0] * n

        def dfs(node):
            if state[node] != 0:
                return state[node] == 2  # safe if previously marked safe

            state[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):  # if any neighbor is unsafe
                    return False
            state[node] = 2  # mark as safe
            return True

        return [i for i in range(n) if dfs(i)]

        