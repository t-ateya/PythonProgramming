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

    def traverseCDLL(self):
        """Traverses the entire CDLL and prints the values"""
        if self.head is None:
            print("The Doubly Linked List is empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def reverse_traversal(self):
        """Traverses the CDLL in reverse order and prints the node values"""
        if self.head is None:
            print("There's no node for reverse traversal")
        else:
            lastNode = self.tail
            while lastNode:
                print(lastNode.value)
                lastNode = lastNode.prev
                if lastNode == self.head.prev:
                    break

    
    def searcNode(self, nodeValue):
        """Searches a given node value in the CDLL and returns all occurrences of the value in the CDLL. My method."""
        if self.head ==None:
            print("There's no element in the CDLL to search")
        else:
            tempNode = self.head 
            while tempNode:
                if tempNode.value == nodeValue:
                    print(tempNode.value)
                if tempNode == self.tail:
                    print(f"The element {nodeValue} is not found")
                    break
                tempNode = tempNode.next


    def searchCDLL(self,nodeValue):
        """Searches the value of an an element in the CDLL"""
        if self.head is None:
            return( "There is not any node in CDLL")
        else:
            temp_node = self.head 
            while temp_node:
                if temp_node.value == nodeValue:
                    return(temp_node.value)
                if temp_node == self.tail:
                    return (f"The value {nodeValue} does not exist in the CDLL")
                temp_node =temp_node.next


    def delete_node(self, location):
        """This method deletes a node from a CDLL. Enter 0 to delelte first element and -1 to delete last element"""
        if self.head == None:
            print("The CDLL is empty.There's no element to delete")
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next 
                    self.head.next.prev = self.tail
                    #self.head.prev = None 
                    #self.head.next = None

            elif location == -1:
                if self.head == self.tail:
                    self.head =None
                    self.tail = None 
                else:
                    currentNode = self.head 
                    prevNode = self.head
                    while currentNode is not self.tail:
                        prevNode = currentNode
                        currentNode = currentNode.next
                    #print(currentNode.value)
                    #print(prevNode.value)
                    currentNode.next = None 
                    currentNode.prev = None 
                    self.tail = prevNode
                    prevNode.next =self.head 
            else:
                #Check if the location is out 
                node_count = 0
                temp_node = self.head 
                while temp_node:
                    temp_node = temp_node.next 
                    node_count +=1
                    if temp_node == self.head:
                        break     
                if location >= node_count:
                    print(f"location is out range: The location {location} must be less than {node_count} nodes")             
                else:
                    index = 0
                    tempNode = self.head 
                    while index < location -1 :
                        tempNode = tempNode.next
                        index += 1
                    print(tempNode.value)
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode 

                    

     
cDLL = CircularDoublyLinkedList()
#print(cDLL.create_CDLL(9))
cDLL.create_CDLL(9)
cDLL.insert_CDLL(11,0)
cDLL.insert_CDLL(12,1)
cDLL.insert_CDLL(13,2)
cDLL.insert_CDLL(14,-1)

print([node.value for node in cDLL ])
cDLL.delete_node(3)
#cDLL.insert_CDLL(12,0)
#cDLL.delete_node(0)

"""
cDLL.insert_CDLL(15,-1)
cDLL.insert_CDLL(17,-1)
cDLL.insert_CDLL(23,4)
cDLL.insert_CDLL(25,-1)
cDLL.insert_CDLL(35,-1)
"""

print([node.value for node in cDLL ])


#cDLL.traverseCDLL()
#cDLL.reverse_traversal()

#cDLL.searcNode(35)
#print(cDLL.searchCDLL(35))