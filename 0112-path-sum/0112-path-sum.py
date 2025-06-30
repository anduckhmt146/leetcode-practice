class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, total):
            if root is None:
                return False

            # Add the current node's value to the total sum
            total -= root.val
            
            # If we are at a leaf node, check if the sum equals targetSum
            if root.left is None and root.right is None:
                return total == 0
            
            # Otherwise, continue the DFS search for left and right subtrees
            return dfs(root.left, total) or dfs(root.right, total)

        # Miễn chỗ này trả về theo root -> targetSum là được
        return dfs(root, targetSum)
