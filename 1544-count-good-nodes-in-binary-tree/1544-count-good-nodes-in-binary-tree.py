# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, prev_max):
            nonlocal count
            if not node:
                return False

            # What node do
            if node.val >= prev_max:
                prev_max = node.val
                count += 1

            # What left right do for root
            left = dfs(node.left, prev_max)
            right = dfs(node.right, prev_max)
            return left and right

        dfs(root, root.val)
        return count



        