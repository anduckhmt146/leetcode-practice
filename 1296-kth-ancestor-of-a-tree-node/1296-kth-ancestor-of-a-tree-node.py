from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = 20  # Enough for trees with up to around 10^6 nodes
        self.dp = [[-1] * self.LOG for _ in range(n)]

        # Initialize each node's direct parent (2^0-th ancestor)
        for i in range(n):
            self.dp[i][0] = parent[i]

        # Fill in the dp table for all 2^j-th ancestors
        for j in range(1, self.LOG):
            for i in range(n):
                prev_ancestor = self.dp[i][j - 1]
                if prev_ancestor != -1:
                    self.dp[i][j] = self.dp[prev_ancestor][j - 1]

        print(self.dp)

    def getKthAncestor(self, node: int, k: int) -> int:
        power = 0
        while k > 0 and node != -1:
            if k % 2 == 1:
                node = self.dp[node][power]
            k //= 2
            power += 1
        return node

        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)