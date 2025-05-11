# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = []
        queue = deque([root])

        # NOTES: Each level we declare here
        currLevel = 1
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()

                if not node.left and not node.right:
                    return currLevel
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            currLevel += 1
        
        return 1
        