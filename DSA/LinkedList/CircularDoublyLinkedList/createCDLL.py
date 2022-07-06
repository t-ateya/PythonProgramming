from node import Node

class CircularDoublyLinkedList:
    def __init__(self):
        self.head  = None 
        self.tail = None 


    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node= node.next 
            if node == self.tail.next:
                break 


    def create_CDLL(self, nodeValue):
        """Creates a new node for any given node value"""
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode 
        newNode.next = newNode 
        newNode.prev = newNode 
        return "The CDLL is created successfully"


    



cDLL = CircularDoublyLinkedList()
print(cDLL.create_CDLL(9))

print([node.value for node in cDLL ])