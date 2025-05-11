# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        maxSum = float('-inf')
        maxLevelSum = 0
        
        currLevel = 0
        
        while queue:
            level_size = len(queue)

            # NOTES: Each level we declare here
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            currLevel += 1
            
            if sum(level_nodes) > maxSum:
                maxSum = sum(level_nodes)
                maxLevelSum = currLevel
        
        return maxLevelSum
        