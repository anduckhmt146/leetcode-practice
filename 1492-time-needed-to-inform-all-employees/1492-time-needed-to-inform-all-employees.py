class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                tree[mgr].append(emp)

        def dfs(emp_id):
            max_time = 0
            for subordinate in tree[emp_id]:
                max_time = max(max_time, dfs(subordinate))
            return informTime[emp_id] + max_time

        return dfs(headID)
            