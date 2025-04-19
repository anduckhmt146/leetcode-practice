class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # smallest so far
            elif num <= second:
                second = num  # second smallest
            else:
                # found a number greater than both -> triplet exists
                return True

        return False