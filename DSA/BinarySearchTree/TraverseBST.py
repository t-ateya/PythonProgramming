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

print("===============Traversing================")
#preOrderTraversal(newBST)
#inOrderTraversal(newBST)
#postOrderTraversal(newBST)
levelOrderTraversal(newBST)



"""
print(newBST.data)
print(newBST.leftChild.data)
"""



