class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        i = 0
        n = len(heights)
        while i < n:
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                right = i - 1
                left = stack[-1] if stack else -1
                area = heights[top] * (right - left)
                max_area = max(max_area, area)

        # Second pass: clean up remaining elements in stack
        # Make sure the stack is increment (2,4,6)
        while stack:
            top = stack.pop()
            right = n - 1
            left = stack[-1] if stack else -1
            area = heights[top] * (right - left)
            max_area = max(max_area, area)

        return max_area

        