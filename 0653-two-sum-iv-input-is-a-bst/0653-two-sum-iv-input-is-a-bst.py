# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Step 1: In-order DFS traversal to get sorted list
        def in_order(node):
            if not node:
                return []
            return in_order(node.left) + [node.val] + in_order(node.right)

        nums = in_order(root)

        # Step 2: Two-pointer technique to find if two numbers sum to k
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False
