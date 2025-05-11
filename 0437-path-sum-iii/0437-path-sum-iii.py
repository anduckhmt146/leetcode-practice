# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from collections import defaultdict

class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # base case: empty path has sum = 0
        self.count = 0

        def dfs(node, current_sum):
            if not node:
                return

            current_sum += node.val

            # Check if there is a prefix path we can subtract to reach targetSum

            # IDEA: current_sum = sum from the root to the current node
            # If there exists a prefix_sum = current_sum - targetSum, then
            # the subpath from after that earlier prefix to the current node must sum to targetSum.

            # IDEA: Sum root -> m subtract for root -> n = targetSum => n -> m is the prefix path
            self.count += prefix_sum[current_sum - targetSum]

            # Add current sum to prefix sums
            prefix_sum[current_sum] += 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Backtrack: remove current sum from the map
            prefix_sum[current_sum] -= 1

        dfs(root, 0)
        return self.count
