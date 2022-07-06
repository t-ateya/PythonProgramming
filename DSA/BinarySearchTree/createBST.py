"""
    BST Additional Properties
    1. In the left subtree, the value of a node is less than or equal its parent node's value
    2. In the right subtree, the value of the node is greater than the parent node's value

    Why BST?
    -It performs faster than Binary Tree when inserting and deleting nodes

    *BST Operations:
    -Creation of Tree
    -Insertion of node
    -Deletion of node
    -Search for a value
    -Traverse all nodes
    -Deletion of tree

"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 




newBST = BSTNode(None)