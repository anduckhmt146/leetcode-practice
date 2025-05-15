class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w/q, q) for q, w in zip(quality, wage)])
    
        heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)  # Max heap by pushing negative
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)  # Remove largest quality (least efficient)
            
            if len(heap) == k:
                cost = total_quality * ratio
                min_cost = min(min_cost, cost)
        
        return min_cost
