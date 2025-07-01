class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []
        result = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = i - top

            stack.append(i)

        return result

        