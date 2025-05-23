class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both arrays
        g.sort()
        s.sort()

        # Two pointers for greed factors and cookie sizes
        child = cookie = 0

        # Try to satisfy each child with the smallest sufficient cookie
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # Cookie satisfies this child
                child += 1
            # Move to the next cookie
            cookie += 1

        return child