
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

    def traversal_DLL(self):
        """Traverses the entire Doubly Linked List and prints the node values"""
        if self.head == None:
            print("The DLL is empty")
        else:
            tempNode = self.head
            while tempNode:
                print(f"{tempNode.data}")
                tempNode = tempNode.next
    

    def reverse_traversal(self):
        """Traverses the doubly linked list in reverse order and prints the node values"""
        tempNode = self.tail 
        while tempNode is not None:
            print(tempNode.data)
            tempNode = tempNode.prev

    def searchDLL(self, nodevalue):
        """searches and node in a DLL and prints it out"""
        if self.head is None:
            print("The node is empty. You can't search an empty DLL")
        else:
            tempNode = self.head 
            while tempNode.next is not None:
                if tempNode.data == nodevalue:
                    print(f"{tempNode.data}")
                tempNode = tempNode.next
            print(f"{nodevalue} is not found in the node")


    def deleteDLL(self, nodeLocation):
        """Deletes an element from the DLL. Enter 0 to delete first element and -1 to delete last element"""
        if self.head is None:
            print("The the list is empty. There's no node to be deleted")
            return 
        if nodeLocation == 0:
            #Find out if there exist just a single node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        elif nodeLocation == -1:
            #Check if there exists a single element in the list
            if self.head == self.tail:
                self.head = None 
                self.tail = None 
            else:
                #Delete last node in multiple nodes
                currentNode= self.head 
                prevNode = self.head
                while currentNode.next is not None:
                    prevNode = currentNode
                    currentNode = currentNode.next
                prevNode.next  = None 
                currentNode.prev = None 
                self.tail = prevNode
        else:
            #Check for out of range deletion
            node_count = 1
            tempNode = self.head
            while tempNode.next is not None:
                node_count +=1
                tempNode = tempNode.next 
            #print(f"Nodes: {node_count}") 

            if nodeLocation >= node_count-1:
                print("The location is out of range")
                return 
            #Delete middle nodes
            tempNode = self.head 
            index = 0
            while index < nodeLocation -1:
                tempNode = tempNode.next 
                index +=1
            tempNode.next = tempNode.next.next 
            tempNode.next.prev = tempNode


    

dLL = DoublyLinkedList()

#dLL.searchDLL(21)

dLL.createDLL(5)
dLL.insertNode(0,0)
dLL.insertNode(2,-1)
dLL.insertNode(6,2)
dLL.insertNode(8,3)

print([node.data for node in dLL])
dLL.deleteDLL(-1)
#dLL.deleteDLL(-1)
#dLL.insertNode(5,-1)
#dLL.insertNode(6,3)

print([node.data for node in dLL])
#dLL.searchDLL(9)
#dLL.traversal_DLL()
#dLL.reverse_traversal()

