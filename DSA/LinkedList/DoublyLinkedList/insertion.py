
from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.head = None 
    
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 

    #Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        """This method creates a DLL"""
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node 
        self.tail = node 
        return "The DLL is created successfully"

    #Insertion of a node into a DLL
    def insertNode(self,nodeValue, location):
        """Inserts a new node into a given location. Enter 0 to insert at the beginning and -1 to insert at the end of the list"""
        #1. Check if a node is created before inserting
        if self.head == None:
           return self.createDLL(nodeValue)
           
        newNode = Node(nodeValue)
        #2. Insertion at the first positon
        if location == 0:
            # Case 2.1: There exists  a single node
            if self.head == self.tail:
                newNode.next = self.head
                newNode.prev = None
                self.head = newNode
                self.tail = newNode.next

            #Case 2.2: There exists many nodes
            else:
                newNode.next = self.head
                self.head = newNode
                newNode.prev = None
        #3. Insert to the end of the DLL
        elif location == -1:
            # Case 3.1: There exists  a single node
            if self.head == self.tail:
                newNode.next = None
                newNode.prev = self.head 
                self.head.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head 
                while tempNode.next is not None:
                    tempNode = tempNode.next
                newNode.next = None
                self.tail = newNode
                newNode.prev = tempNode
                tempNode.next = newNode
        else:
            #Case 4: Insertion at the middle of the DLL
            nodeCount = 0 
            tempNode = self.head
            while tempNode != None:
                tempNode = tempNode.next
                nodeCount +=1
            if location >= nodeCount:
                print(" Sorry!!! The location is out of range\n")
                print(f"There are {nodeCount} nodes. The location {location} is out of range")
            else:
                
                temp2 = self.head
                index = 0
                while index < location -1:
                    temp2 = temp2.next 
                    index +=1 
                newNode.next = temp2.next 
                temp2.next.prev = newNode
                newNode.prev = temp2
                temp2.next = newNode

    

dLL = DoublyLinkedList()
dLL.insertNode(1,0)
dLL.insertNode(2,-1)
dLL.insertNode(3,-1)
dLL.insertNode(5,-1)
dLL.insertNode(6,3)
dLL.insertNode(6,0)
dLL.insertNode(7,5)
#dLL.createDLL(5)
#dLL.createDLL(10)

print([node.data for node in dLL])

