class BinaryTree:
    def __init__(self, size):
        self.customList = size*[None]
        self.maxSize = size 
        self.lastUsedIndex = 0
        self.success = "SUCCESS"
        self.notFound = "NOT FOUND"
    

    def insertBT(self, value):
        """Inserts data in a BT at a specific position"""
        if self.lastUsedIndex + 1  == self.maxSize:
            return "The BT is Full"
        else:
            self.lastUsedIndex +=1
            self.customList[self.lastUsedIndex] = value
            return "The value has been inserted successfully"

    
    def searchNode(self, nodeValue):
        if self.customList == self.maxSize*[None]:
            return "The BT is empty"
        else:
            for node in self.customList:
                if node == nodeValue:
                    return self.success
            
            return self.notFound

    
    def preOrderTraversal(self, index):
        """Visit rootNode->leftChild->RightChild"""
        if (index > self.lastUsedIndex):
            return 
        print(self.customList[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index + 1)

    def inOrderTraversal(self, index):
        """Visit left SubTree->RootNode->Right SubTree"""
        if (index > self.lastUsedIndex):
            return 
        self.inOrderTraversal(2*index)
        print(self.customList[index])
        self.inOrderTraversal(2*index + 1)


    def postOrderTraversal(self, index):
        """Visit left SubTree->Right SubTree->RootNode"""
        if (index > self.lastUsedIndex):
            return 
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index + 1)
        print(self.customList[index])


    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])


    
        
                


            





newBT = BinaryTree(8)

newBT.insertBT("Drinks")
newBT.insertBT("Hot")
newBT.insertBT("Cold")
newBT.insertBT("Tea")
newBT.insertBT("Coffee")

#newBT.preOrderTraversal(3)
#newBT.postOrderTraversal(1)
newBT.levelOrderTraversal(1)


