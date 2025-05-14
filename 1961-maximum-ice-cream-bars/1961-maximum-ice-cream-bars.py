class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0

        for price in costs:
            if coins < price:
                break
            coins -= price
            count += 1

        return count


        