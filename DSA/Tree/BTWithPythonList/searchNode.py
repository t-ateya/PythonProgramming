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
            self.customList[self.lastUsedIndex] = value
            self.lastUsedIndex +=1
            return "The value has been inserted successfully"

    
    def searchNode(self, nodeValue):
        if self.customList == self.maxSize*[None]:
            return "The BT is empty"
        else:
            for node in self.customList:
                if node == nodeValue:
                    return self.success
            
            return self.notFound
                


            





newBT = BinaryTree(8)

print(newBT.insertBT("Drink"))
print(newBT.insertBT("Hot"))
print(newBT.insertBT("Cold"))

print("=====Search Node=====")
print(newBT.searchNode("Tea"))


