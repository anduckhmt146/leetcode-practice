class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        return sum(p / t for _, p, t in heap) / len(classes)
        