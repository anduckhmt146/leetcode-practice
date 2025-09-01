# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        
        def preorder(node):
            if not node: 
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return " ".join(vals)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: 
            return None

        vals = list(map(int, data.split()))
        self.i = 0
        
        def build(lower, upper):
            if self.i == len(vals): 
                return None
            val = vals[self.i]
            if not (lower < val < upper): 
                return None
            self.i += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node
        
        return build(float('-inf'), float('inf'))
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans