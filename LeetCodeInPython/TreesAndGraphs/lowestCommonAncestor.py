"""
    #Medium
    Lowest common ancestor of a binary tree
    Given a binary tree, find the lowest common ancestor(LCA) of two given nodes in the tree.
    The lowest common ancestor is defined between two nodes p and q as the lowest node in the tree that has p and q as descendants.
    Note: We allow a node to be a descendant of itself.
"""
class TreeNode:
    def __init__(self, x) -> None:
        self.right = None 
        self.left = None 
        self.val = x 


class Solution:
    def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode)->TreeNode:
        if (root is None):
            return root 
        
        if(root.val == p.val or root.val == q.val ):
            return root 

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left is None and right is None):
            return None 

        if (left and right):
            return root 

        return right if left is None else left 
        

        