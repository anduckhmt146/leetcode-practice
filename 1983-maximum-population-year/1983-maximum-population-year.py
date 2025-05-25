from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101  # years 1950 to 2050 → index 0 to 100

        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1

        max_pop = year = 0
        current_pop = 0

        for i in range(101):
            current_pop += population[i]
            if current_pop > max_pop:
                max_pop = current_pop
                year = 1950 + i

        return year
