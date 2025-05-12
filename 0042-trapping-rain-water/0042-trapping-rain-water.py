from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                top = stack.pop()

                if not stack:
                    break  # No left boundary to trap water

                # Distance (width) between the left and right boundaries
                distance = i - stack[-1] - 1

                # Height of water above the current bar
                # Area of 2 rectangle - Area of bottom valley
                bounded_height = min(height[stack[-1]], height[i]) - height[top]

                # Add trapped water
                water += distance * bounded_height

            stack.append(i)

        return water
