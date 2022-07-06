"""
    1. Creation of Tree
    2. Insertion of a node
    3. Deletion of a node
    4. Search for a value
    5. Traverse all nodes
    6. Deletion of tree

    Here, we will create a binary tree using a linked list
"""

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 