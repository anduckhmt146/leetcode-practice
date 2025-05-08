"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Create a mapping from id to employee object for quick lookup
        emp_map = {employee.id: employee for employee in employees}
        
        def dfs(emp_id: int) -> int:
            employee = emp_map[emp_id]
            total_importance = employee.importance
            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)
            return total_importance
        
        return dfs(id)
        