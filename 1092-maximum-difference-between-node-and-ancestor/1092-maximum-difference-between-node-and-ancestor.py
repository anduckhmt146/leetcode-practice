# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # cur_max and cur_min flow only along one path at a time.
        # When we go down the left subtree (5 → 3 → 1), the state is isolated to that path.
        # When we go down the right (5 → 8 → 10), it’s a separate set of state values.
        def dfs(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min
            
            # Update current max and min
            # I mean curr_max and curr_min is reset based on different path (left or right)
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            
            # Continue DFS traversal
            left = dfs(node.left, cur_max, cur_min)
            right = dfs(node.right, cur_max, cur_min)
            
            return max(left, right)
        
        return dfs(root, root.val, root.val)
        