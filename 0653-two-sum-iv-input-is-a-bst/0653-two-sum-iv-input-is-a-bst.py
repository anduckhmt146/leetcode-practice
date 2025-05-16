# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return k == 0
        
        result = []
        queue = deque([root])

        # When out the loop 
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        numToIndex = {}
        for pE in range(0, len(result)):
            currVal = result[pE]

            if k - currVal in numToIndex:
                return True

            numToIndex[currVal] = pE

        return False
        