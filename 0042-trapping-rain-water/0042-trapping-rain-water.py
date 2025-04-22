class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water_trapped = 0

        for i in range(0, len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                width = i - stack[-1] - 1  
                bounded_height = min(height[i], height[stack[-1]]) - height[top] 
                water_trapped += width * bounded_height

            stack.append(i)

        return water_trapped
            
        