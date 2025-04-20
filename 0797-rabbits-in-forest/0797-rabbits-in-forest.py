from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # If a rabbit says "x other rabbits have the same color," it means there are x + 1 total rabbits of that color.
        # But if multiple rabbits say the same number, they might be in the same group, or represent multiple groups of that same size.
        counter = Counter(answers)
        count = 0

        for key, freq in counter.items():
            group_size = key + 1
            groups = math.ceil(freq / group_size)
            count += groups * group_size

        return count




        