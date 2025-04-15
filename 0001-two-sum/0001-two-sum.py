from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N * logN)
        
        # Pair each number with its index
        nums_with_indices = list(enumerate(nums))  # [(index, value)]

        # Sort based on the values
        nums_with_indices.sort(key=lambda x: x[1])

        start, end = 0, len(nums_with_indices) - 1

        while start < end:
            curr_sum = nums_with_indices[start][1] + nums_with_indices[end][1]
            
            if curr_sum == target:
                return [nums_with_indices[start][0], nums_with_indices[end][0]]
            elif curr_sum < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]



        