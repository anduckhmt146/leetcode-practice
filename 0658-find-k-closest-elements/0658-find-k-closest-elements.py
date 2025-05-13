import heapq

class Solution:
    # Max Heap
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Use a max-heap (invert distances)
        max_heap = []

        for num in arr:
            dist = -abs(num - x) # invert to simulate max-heap
            heapq.heappush(max_heap, (dist, -num))

            # Because it push larger, remove the smaller first => reverse to remove the larger first, push smaller later
            if len(max_heap) > k:
                # IDEA: Python's heapq is a min-heap by default, meaning:
                # IDEA: It always keeps the smallest element at the top (heap[0]), here is dist
                heapq.heappop(max_heap)

        # Extract only the arr from the heap
        result = [-num for _, num in max_heap]
        # Why -num? 
        # This ensures that when two numbers have the same distance from x, the smaller number is preferred — as required by the problem.
        result.sort()
        return result
        