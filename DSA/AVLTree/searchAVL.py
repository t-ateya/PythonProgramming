
import LinkedList as ll



class AVLNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 
        self.height = 1



def preOrderTraversal(rootNode):
    """RootNode->LeftNode->RightNode"""
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    """LeftSubTree->RootNode->RightSubTree"""
    if rootNode is None:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    """LeftSubTree->RightSubTree->RootNode"""
    if rootNode == None:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    customQ = ll.Queue()
    customQ.enqueue(rootNode)
    while not customQ.isEmpty():
        root = customQ.dequeue()
        print(root.value.data)

        if root.value.leftChild:
            customQ.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQ.enqueue(root.value.rightChild)

def searchBSTNode(rootNode, nodeValue):
    """Searchs for a node in BST"""
    
    if rootNode.data == nodeValue:
        print ("Value Found")
    
    elif rootNode.leftChild and nodeValue < rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            print("Value Found")
        else:
            searchBSTNode(rootNode.leftChild, nodeValue)
    elif rootNode.rightChild and nodeValue > rootNode.data:
        if nodeValue == rootNode.rightChild.data:
            print ("Value Found")
        else:
            searchBSTNode(rootNode.rightChild, nodeValue)
    else:
        print("Not Found")

            

newAVL  = AVLNode(10) 

