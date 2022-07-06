class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None
        

    def __str__(self):
        return str(self.value)



class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        currentNode = self.head 
        while currentNode:
            yield currentNode
            currentNode = currentNode.next



class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
       values=  [str(element) for element in self.linkedList]
       return ' '.join(values)


    def enqueue(self, value):
        """Adds an element to the queue"""
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node 
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    
    def isEmpty(self):
        """"Returns True if the Queue is empty. Otherwise False"""
        if self.linkedList.head == None:
            return True 
        else:
            return False

    def dequeue(self):
        """Removes an element from the Queue"""
        if self.isEmpty():
            return "The Queue is empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode


    def peek(self):
        """Returns the first value in the Queue"""
        if self.isEmpty():
            return "The Queue is empty"
        else:
            return self.linkedList.head
            

    def delete(self):
        """Deletes the entire queue"""
        self.linkedList.head = None 
        self.linkedList.tail = None 