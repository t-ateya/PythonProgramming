
"""
    Validate BST - LeetCode 98

    Implement a function to check if a binary tree is a Binary Search Tree

    Solution:
    A binary tree is a binary search tree iff:
        - The left subtree of a node contains only nodes with keys less than the node's key
        - The right subtree of a node contains only nodes with keys less than the node's key
        - These conditions are applicable for both left and right subtrees
"""

class TreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = None 
        self.right = None 
    
def helper(node, min_value = float('-inf'), max_value = float('inf')):
    if not node:
        return True 
    
    val = node.value 
    if val <= min_value or val >= max_value:
        return False 

    if not helper(node.right, val, max_value ):
        return False

    if not helper(node.left, min_value, val):
        return False

    return True

def is_valid_BST(root):
    return help(root)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root1.right = TreeNode(root1)

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

print(is_valid_BST(root2))
