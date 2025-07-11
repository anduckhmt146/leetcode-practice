class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2

        # Init start
        start = 0
        n = len(fruits)
        state = {}
        max_len = 0
        
        # Counting
        for end in range(n):
            state[fruits[end]] = state.get(fruits[end], 0) + 1

            # Prunning
            while len(state) > 2:
                # Update start
                state[fruits[start]] -= 1
                if state[fruits[start]] == 0:
                    del state[fruits[start]]
                start += 1
            
            max_len = max(max_len, end - start + 1)

        return max_len

