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


    def insert_CDLL(self, value, location):
        """This method inserts a given node data a specific location in a DLL with 0 being first location and 1 last location"""
        if self.head == None:
            return "The CDLL does not exist"
        
        else:
            newNode = Node(value)
            if  location == 0:
                #Case 1: There exist a single node
                if self.head == self.tail:
                    newNode.next = self.head 
                    newNode.prev = self.tail
                    self.head.prev = newNode
                    self.head = newNode
                    self.tail.next = newNode
                else:
                    newNode.next = self.head 
                    self.head.prev = newNode
                    self.head = newNode
                    self.tail.next = newNode
            elif location == -1:
                #Check if there just one node
                if self.head == self.tail:
                    newNode.prev = self.tail
                    newNode.next = self.head
                    self.head.next = newNode
                    self.tail = newNode
                else:
                    #Case where the CDLL consist of many nodes
                    tempNode = self.head 
                    while tempNode is not self.tail:
                        tempNode = tempNode.next
                    tempNode.next = newNode
                    newNode.prev = self.tail
                    newNode.next = self.head 
                    self.tail = newNode
            else:
                #Insertion in the middle of the CDLL
                node_count = 1
                firstNode = self.head 
                while firstNode != self.tail:
                    firstNode = firstNode.next
                    node_count +=1
                if location >= node_count:
                    print(f"Location out of range. The location entered is: {location} must be less than number of nodes: {node_count}")
                else:
                    index = 0
                    tempNode = self.head
                    while index < location -1:
                        tempNode = tempNode.next
                        index +=1
                    newNode.next = tempNode.next
                    tempNode.next.prev = newNode
                    tempNode.next = newNode
                    newNode.prev = tempNode

    


cDLL = CircularDoublyLinkedList()
#print(cDLL.create_CDLL(9))
cDLL.create_CDLL(9)
cDLL.insert_CDLL(11,-1)
cDLL.insert_CDLL(12,0)
cDLL.insert_CDLL(15,-1)
cDLL.insert_CDLL(17,-1)
cDLL.insert_CDLL(23,4)
cDLL.insert_CDLL(25,-1)


print([node.value for node in cDLL ])

cDLL.traverseCDLL()