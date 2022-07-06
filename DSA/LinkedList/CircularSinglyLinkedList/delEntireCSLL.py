
from node import Node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next
            if node == self.tail.next:
                break
            
    #Creation of a circular singly linked list
    def create_CSLL(self, value):
        """This method creates a Circularly linked list with given data value"""
        node = Node(value)
        self.head = node
        self.tail = node 
        node.next = node 
        return "The CSLL has been created"


    def insert_CSLL(self, value, position):
        """Insert a value at any given position with 0 being first position and -1 last position. The value is inserted to last position by default"""

        """
        if self.head == self.tail == None:
            self.create_CSSL(value)
        """
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if position == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next= newNode
            elif position == 1:
                newNode.next = self.tail.next  #connection between last node and first node
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode 
                newNode.next = nextNode
            return "The node has been successfully inserted"

    def traversalCSLL(self):
        """This method traverses the CSLL and prints the node value"""
        if self.head is None:
            return "The CSLL is empty. No element in the list for traversal"
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break
    
    #searching for a node in circular singly linked list
    def search_CSLL(self, nodeValue):
        """Searchs for an element in a CSLL and returns its value"""
        if self.head == None:
            return "The CSLL is empty. No node!!!"
        else:
            temp_node = self.head 
            while temp_node:
                if temp_node.value == nodeValue:
                    return f"{nodeValue}"
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return f"{nodeValue} not found"

    
    def deleteCSLL(self, location):
        """"Deletes at a given location from a CSLL. First element is location 0 and last element location -1"""
        #0. Check if the CSLL has a node
        if self.head is None:
            return "The CSLL has no node(element) to be deleted"

        #Case 1: Deleting the first node
        if location == 0:
            #1.1: List contains just one node
            if self.head == self.tail:
                first = self.head 
                self.head = None
                self.tail = None
                first.next = None 
            #1.2: List contains more than one node
            elif self.head is not self.tail:
                firstNode = self.head
                self.head = firstNode.next 
                lastNode = self.tail
                lastNode.next = firstNode
        #Case 2: Deleting the last element      
        elif location == -1 and self.head is not self.tail:
            currentNode = self.head
            while currentNode:
                prevNode = currentNode
                currentNode = currentNode.next
                if currentNode == self.tail.next:
                    self.tail = prevNode
                    prevNode.next = self.head
        #Case 3:  Deleting a node in the middle of the CSLL
        elif location == -1 and self.head == self.tail:  #There exist just one element in the CSLL
            firstNode = self.head
            self.head = None
            self.tail = None
            firstNode.next = None
        else:
            #3.1: Check if the location is out of range
            tempNode = self.head 
            nodeCount = 1
            while tempNode:
                tempNode = tempNode.next
                nodeCount +=1
                if tempNode == self.tail.next:
                    break
            if nodeCount >= location:
                return f"Sorry!!!. The location {location} is out of range"
            else:
                currentNode = self.head 
                index = 0
                while index < location -1:
                    prevNode = currentNode
                    currentNode= currentNode.next
                    index += 1
                prevNode = currentNode.next
    

    #Delete a node from a Circular Singly Linked List
    def deleteNode(self, location):
        """Deletes a node from CSLL"""
        if self.head is None:
            return "There's no node to be deleted"
        else:
            if location == 0:
                #1.List contains one element
                if self.head == self.tail:
                    self.head.next = None  
                    self.head = None 
                    self.tail = None 
                else:
                    #2. List contains more than one element
                    self.head = self.head.next
                    self.tail.next = self.head 
            elif location == 1: #Del element from the end of the CSLL
                #Check if it's a single node
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None 
                    self.tail = None 
                else:
                    currentNode = self.head
                    while currentNode is not None:
                        if currentNode.next == self.tail.next:
                            break
                        currentNode = currentNode.next
                    currentNode.next = self.head
                    self.tail = currentNode
            else:
                #Delete an element in the middle of the CSLL
                index  = 0 
                tempNode = self.head 
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                #tempNode = tempNode.next.next
                nextNode = tempNode.next
                tempNode.next = nextNode.next 

                    
    def deleteEntireCSLL(self):
        """Deletes all elements from a CSLL"""
        if self.head is None:
            return "The CSLL is empty. No element to delete"
        self.head = None 
        self.tail.next = None 
        self.tail = None 

    
cSLL = CircularSinglyLinkedList()
print(cSLL.create_CSLL(1))

cSLL.insert_CSLL(0,0)
cSLL.insert_CSLL(2,1)
cSLL.insert_CSLL(3,1)
cSLL.insert_CSLL(2,2)

#List comprehension
print([(node.value) for node in cSLL])

cSLL.traversalCSLL()