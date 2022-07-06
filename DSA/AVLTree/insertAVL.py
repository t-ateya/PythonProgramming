
import LinkedList as ll

"""
    Insertion in AVL:
            AVL is balanced if: (Height(LeftSubTree) - Height(RightSubTree) in [-1, 1]))
        Case 1. Rotation is not required
        Case 2. Rotation is required
                    Rotation condition is determined by considering the path to the Grand Child of the unbalancedNode
                    N.B: If we have both Left and Right Grand Children, we consider the path to the Grand Child with more height
             LL -Left left condition =>Right Rotation of unbalancedNode
             LR - Left Right condition
                1. Left Rotation of the left child of unbalanced node (rotate left disbalancedNode.leftChild)
                2. and then Right Rotation of the unbalanced node (Rotate Right disbalancedNode)
             RR - Right Right condition
                        - Perform Left Rotation of unbalancedNode (Rotate Left DisbalancedNode)

             RL - Right Left condition
                  1. Right Rotation
                        Right rotation of the right child of the inbalancedNode (rotate right disbalancedNode.rightChild)
                  2. LeftRotation
                        and then left rotation of the unbalanced Node (Rotate left disbalancedNode)
"""
class AVLNode:
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
    

def getHeight(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height

def rightRotate(disbalancedNode):
    """The function rotates any disbalanced node to the right"""
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disbalancedNode):
    """Rotates any unbalanced node to the left"""
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild  = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    """Inserts new node into the avl"""
    if not rootNode:
        return AVLNode(nodeValue)
    elif  nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    #1. LL condition
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    #2. LR conditon
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    #3.RR condition
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    #4. RL condition
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


    
newAVL  = AVLNode(5) 
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelOrderTraversal(newAVL)

