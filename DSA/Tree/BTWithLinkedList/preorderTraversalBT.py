"""
    Traversal of Binary Tree

Depth first search
    -Preorder Traversal-visit rootNode, then LeftSubTree and lastly, RightSubTree
    -Inorder traversal
    - Post order Traversal
Breadth first search
 - Level order traversal

"""

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


preOrderTraversal(newBT)