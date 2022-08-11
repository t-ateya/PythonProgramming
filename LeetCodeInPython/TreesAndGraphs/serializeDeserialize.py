"""
    #Hard 297
    Serialize and deserialize binary tree.
    Design an algorithm to serialize and deserialize a binary tree.

    Serialization is the process of converting a data structure or object into sequence of bits.
    Deserialization is the process of converting that sequence of bits to the original datastructure.
"""

class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None 
        self.right = None 


class Codec:
    def serialize(self, root:TreeNode):
        if not root:
            return "X#"

        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        return str(root.val) + '#' + leftSerialized+rightSerialized

    def deserialize(self, data):
        
        def dfs():
            val = next(data);
            if val == 'X':
                return None 
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node 

        data = iter(data.split('#'))
        return dfs()

            