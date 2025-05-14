class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = sorted([a, b, c])
        # If the sum of the two smaller piles is less than or equal to the largest,
        # you can only make moves equal to the total of the two smaller ones.
        if stones[0] + stones[1] <= stones[2]:
            return stones[0] + stones[1]
        return int((a + b + c) / 2)
        