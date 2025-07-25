from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # one boat for both
            right -= 1  # heaviest person always goes
            boats += 1

        return boats
