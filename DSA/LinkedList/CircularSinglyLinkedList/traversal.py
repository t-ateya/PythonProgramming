
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






cSLL = CircularSinglyLinkedList()
print(cSLL.create_CSLL(1))

cSLL.insert_CSLL(0,0)
cSLL.insert_CSLL(2,1)
cSLL.insert_CSLL(3,1)
cSLL.insert_CSLL(2,2)

#List comprehension
print([(node.value) for node in cSLL])

cSLL.traversalCSLL()