import heapq
from collections import Counter

class Solution:
    # To avoid having the same characters next to each other, you want to spread out the most frequent characters as evenly as possible.
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        count = Counter(s)

        if any(freq > (len(s) + 1) // 2 for freq in count.values()):
            return ""

        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        prev_freq, prev_char = 0, ''
        result = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            # If the previous character can still be used, push it back
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            # Update previous character to the current one
            prev_freq, prev_char = freq + 1, char  # since freq is negative

        reorganized = ''.join(result)

        # Final check: if the result is valid
        for i in range(1, len(reorganized)):
            if reorganized[i] == reorganized[i - 1]:
                return ""
        
        return reorganized
