class BinaryTree:
    def __init__(self, size):
        self.customList = size*[None]
        self.maxSize = size 
        self.lastUsedIndex = 0
    

    def insertBT(self, value):
        """Inserts data in a BT at a specific position"""
        if self.lastUsedIndex + 1  == self.maxSize:
            return "The BT is Full"
        else:
            self.lastUsedIndex +=1
            self.customList[self.lastUsedIndex] = value
            return "The value has been inserted successfully"
            





newBT = BinaryTree(8)
print(newBT.insertBT("Drink"))
print(newBT.insertBT("Hot"))
print(newBT.insertBT("Cold"))

