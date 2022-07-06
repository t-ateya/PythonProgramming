#1. Insrtion at the beginning of the linked list
#2. After a node in the middle of the linked list
#3. At the end of the linked list

class Node:
    def __init__(self, data =None):
        self.data = data 
        self.next = None


class SLinkedList:
    #None == Null
    def __init__(self):
        self.head = None #stores physical loc
        self.tail = None 

    def __iter__(self):
        """method to print our singly Linked List"""
        node = self.head 
        while node:
            yield node
            node = node.next 

    def insertSLL(self, data, location):
        """Inserts a new node in given location in a linkedList"""
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #insert element at the beginning of SSL
                newNode.next = self.head 
                self.head = newNode #update head with  newNode's physical location
            elif location == 1: #insert element at the end of SSL
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                pos = 0
                tempNode = self.head
                while pos < location -1:
                    tempNode = tempNode.next
                    pos += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def traverseSSL(self):
        """The methods traverses singly linked list and prints the data"""
        if self.head:
            tempNode = self.head
            while tempNode.next != None:
                print(tempNode.data)
                tempNode = tempNode.next
        else:
            print("The singly linked list does not exist")
    def search_value(self, value):
        """Searches for a value and returns its value and position"""

        if self.head is None:
            return "The list does not exist"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.data == value:
                    return f"{value} exists"
                tempNode = tempNode.next
            return f"{value} does not exist in this list"
                    
                
        
            
        

            


singlyLinkedList = SLinkedList()
#print(singlyLinkedList.search_value(1))
#singlyLinkedList.traverseSSL()
singlyLinkedList.insertSLL(1,0)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,2)
singlyLinkedList.insertSLL(4,3)


singlyLinkedList.insertSLL(8,4)

singlyLinkedList.insertSLL(0,5)



print([node.data for node in singlyLinkedList])

#singlyLinkedList.traverseSSL()

print(singlyLinkedList.search_value(9))

