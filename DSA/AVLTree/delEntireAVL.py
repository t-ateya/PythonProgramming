
import LinkedList as ll

"""
    Case 1 - The tree does not exist
                - Return a message saying the node does not exist
    Case 2 - Rotation is not required
        1. Node is leaf Node(Has no children)
           - Traverse and delete node
        2. Node has one child 
             - Delete node
             - Set child of deleted node to child of parent of deleted node
        3. The node has two children
                - Find the successor of the node(by going to the right and then left)
                - Replace the node with its successor (min value from the right subtree)
                - Let the right child of the successor node point to the parent of the successor
        4. Rotation is required
                -Left Left Condition
                -Left Right Condition
                -Right Right Condition
                -Right Left Condition




    Case 3 - Rotation is required (LL, LR, RR, RL)
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


def getSuccessorNode(rootNode):
    """"Returns the minimum node in the right subtree(Successor NODE). My approach"""
    if not rootNode:
        return "The AVL tree is empty"
    else:
        tempNode = rootNode.rightChild
        while tempNode.leftChild:
            tempNode = tempNode.leftChild
        return tempNode


def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild=deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild=deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None 
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None 
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance >1 and getBalance(rootNode.leftChild) >=0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <=0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        return leftRotate(rootNode)
    return rootNode


def delEntireAVL(rootNode):
    """Deletes the entire AVL"""
    rootNode.data = None
    rootNode.rightChild = None 
    rootNode.leftChild = None 
    return "The AVL tree has been successfully deleted"






newAVL  = AVLNode(5) 
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL= insertNode(newAVL, 20)

#newAVL = deleteNode(newAVL, 11)
#levelOrderTraversal(newAVL)

delEntireAVL(newAVL)
levelOrderTraversal(newAVL)


