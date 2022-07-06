
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

            

newAVL  = AVLNode(10) 

