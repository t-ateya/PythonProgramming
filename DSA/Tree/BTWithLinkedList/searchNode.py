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

cappuccinno = TreeNode("Cappuccinno")

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


def searchBT1(rootNode, node):
    """Here we use levelOrderTraversal since it makes use of Queue and queue being efficient. My approach"""
    if not rootNode:
        return 
    else:
        customQ = ll.Queue()
        customQ.enqueue(rootNode)
        while not (customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value is node:
                return root.value.data
            else:
                if (root.value.leftChild is not None):
                    customQ.enqueue(root.value.leftChild)

                if (root.value.rightChild is not None):
                    customQ.enqueue(root.value.rightChild)
        return "The node is not found"


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQ = ll.Queue()
        customQ.enqueue(rootNode)
        while not (customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value.data == nodeValue:
                return "SUCCESS"
            if (root.value.leftChild is not None):
                    customQ.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQ.enqueue(root.value.rightChild)
        return "Not Found"
            




print(searchBT(newBT,8))
