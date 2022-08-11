"""
    Easy #104
    Maximum depth of a binary tree
    Given a binary tree, find the maximum depth of the tree.
    Max depth is the no. of nodes in the longest path from root to furthest lead node
"""

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 


class Solution:
    def maxDepth(self, root: TreeNode)->int:
        if not root:
            return 0

        if (root.left is None and root.right == None):
            return 1

        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)

        return max(right, left) + 1
        