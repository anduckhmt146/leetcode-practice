class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit, and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort the worker abilities
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        i = 0
        
        for ability in worker:
            # Update the best job the worker can do
            while i < len(jobs) and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_profit += max_profit
        
        return total_profit