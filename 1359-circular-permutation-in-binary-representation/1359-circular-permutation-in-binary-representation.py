class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Step 1: Generate the standard Gray code sequence
        gray_codes = [i ^ (i >> 1) for i in range(1 << n)]
        
        # Step 2: Find the index of the starting number
        start_index = gray_codes.index(start)
        
        # Step 3: Rotate the sequence so it starts from `start`
        return gray_codes[start_index:] + gray_codes[:start_index]