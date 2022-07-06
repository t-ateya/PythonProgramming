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

    Traversals:
    1.Depth first Traversal:
        -Preorder Traversal
        -Inorder Traversal
        -PostOrder Traversal
    2. Breath First Traversal
        -LevelOrder Traversal
"""

import LinkedList as ll



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

def minValueNode(bstNode):
    currentNode = bstNode
    while currentNode is not None:
        currentNode = currentNode.leftChild
    return currentNode

def deleteBSTNode(rootNode, nodeValue):
    """
      Three cases:
      1. The node to be deleted is a leaf node
      2. The node has one child 
      3. The node has two children
    """
    if rootNode is None:
        return rootNode
    
    #1. Node is a leafNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteBSTNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteBSTNode(rootNode.rightChild, nodeValue)
    else:
        #Node has one child
        if not rootNode.leftChild:
            temp = rootNode.rightChild
            rootNode = None 
            return temp 

        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp 
        #Node has two Children

        temp = minValueNode(rootNode.rightChild)
        rootNode.data =  temp.data
        rootNode.rightChild = deleteBSTNode(rootNode.rightChild, temp.data)
    return  rootNode
   

    
        
    






newBST = BSTNode(None)

insertBSTNode(newBST,70)
insertBSTNode(newBST,50)
insertBSTNode(newBST, 90)
insertBSTNode(newBST, 30)
insertBSTNode(newBST, 60)
insertBSTNode(newBST, 80)
insertBSTNode(newBST, 100)
insertBSTNode(newBST, 20)
insertBSTNode(newBST, 40)


deleteBSTNode(newBST, 20)
levelOrderTraversal(newBST)







