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



def insertBSTNode(rootNode, nodeValue):
    """This method inserts a node into a BST"""
    newNode = BSTNode(nodeValue)
    if rootNode.data == None:
        rootNode.data = nodeValue


    elif  nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = newNode
        else:
            insertBSTNode(rootNode.leftChild, nodeValue)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = newNode
        else:
            insertBSTNode(rootNode.rightChild, nodeValue)
    return "The node has successfully been inserted"


newBST = BSTNode(None)
print(insertBSTNode(newBST,70))
print(insertBSTNode(newBST,60))

print(newBST.data)
print(newBST.leftChild.data)


