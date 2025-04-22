class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O(N^2)
        # for i in range(len(gas)):
        #     fuel = gas[i] - cost[i]
        #     if fuel < 0:
        #         continue

        #     j = (i + 1) % len(gas)
        #     count = 1

        #     while j != i:
        #         fuel += gas[j] - cost[j]
        #         if fuel < 0:
        #             break
        #         j = (j + 1) % len(gas)
        #         count += 1

        #     if count == len(gas) and fuel >= 0:
        #         return i

        # return -1

        # O(N)
        total_gas = 0
        total_cost = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                # Can't reach this station from previous start
                start = i + 1
                tank = 0

        return start if total_gas >= total_cost else -1
