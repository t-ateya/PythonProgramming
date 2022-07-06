"""
    Traversal of Binary Tree

Depth first search
    -Preorder Traversal-visit rootNode, then LeftSubTree and lastly, RightSubTree
    -Inorder traversal-visit leftChild->RootNode->RightChild
    - Post order Traversal -leftSubTree->RightSubTree-RootNode
Breadth first search
 - Level order traversal

"""
import linkedList as ll

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if rootNode is None:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)



def levelOrderTraversal(rootNode):
    if rootNode == None:
        return 
    else:
        customQueue = ll.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


levelOrderTraversal(newBT)