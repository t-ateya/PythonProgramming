from asyncio.windows_events import NULL
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
        node.prev = NULL
        node.next = NULL
        self.head = node 
        self.tail = node 
        return "The DLL is created successfully"


    

dLL = DoublyLinkedList()
dLL.createDLL(5)
dLL.createDLL(10)

print([node.data for node in dLL])

