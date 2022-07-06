
from node import Node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 


    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            if node.next == self.head:
                break
            node = node.next 

    #Creation of a circular singly linked list
    def create_CSSL(self, value):
        """This method creates a Circularly linked list with given data value"""
        node = Node(value)
        self.head = node
        self.tail = node 
        node.next = node 
        return "The CSLL has been created"



cSLL = CircularSinglyLinkedList()
cSLL.create_CSSL(1)
cSLL.create_CSSL(2)
cSLL.create_CSSL(3)
cSLL.create_CSSL(4)

#List comprehension
print([(node.value) for node in cSLL])