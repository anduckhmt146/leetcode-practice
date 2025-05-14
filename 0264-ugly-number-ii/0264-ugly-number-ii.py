import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        primes = [2, 3, 5]

        for _ in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                new_ugly = ugly * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return ugly

        