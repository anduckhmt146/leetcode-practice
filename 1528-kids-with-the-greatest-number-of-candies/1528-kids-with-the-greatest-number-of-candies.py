class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # O(N)
        maxCandy = max(candies)
        result = []
        for candie in candies:
            isLargerAfterReceiveCandies = candie + extraCandies >= maxCandy
            result.append(isLargerAfterReceiveCandies)

        return result
        