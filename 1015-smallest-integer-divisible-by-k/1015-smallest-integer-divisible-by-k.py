class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # If K is even or divisible by 5, it can never divide a number made of only 1s
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        remainder = 0
        for n in range(1, K + 1):  # We only need to check up to K times
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return n
        
        return -1
