# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, path, target):
            if not node:
                return
            
            path.append(node.val)
            target -= node.val
            if not node.left and not node.right and target == 0:
                result.append(path[:])
            else:
                dfs(node.left, path, target)
                dfs(node.right, path, target)

            # Backtrack
            path.pop()
            target += node.val

        
        dfs(root, [], targetSum)
        return result
        