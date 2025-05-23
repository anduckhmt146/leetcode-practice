class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x

        # Check that x and y are non-negative and valid
        if x < 0 or y < 0 or 4 * x + 2 * y != tomatoSlices or x + y != cheeseSlices:
            return []
        
        return [x, y]