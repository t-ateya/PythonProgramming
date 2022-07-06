from random import randint



class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 


    def __str__(self):
        """Makes our node printable by deciding which property of the node will be printed """
        return str(self.value)



class LinkedList:
    def __init__(self, values = None):
        self.head = None 
        self.tail = None 


    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next 


    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)



    def __len__(self):
        result = 0
        tempNode = self.head
        while tempNode:
            result += 1
            tempNode = tempNode.next 
        return result



    def add(self, value):
        """Adds an element at the end of linked list"""
        if self.head is None:
            newNode = Node(value)
            self.head = newNode 
            self.tail = newNode
        else:
            newNode = Node(value)
            self.tail.next = newNode 
            self.tail = self.tail.next 
        return self.tail

    
    def generate(self, n, min_value, maximum_value):
        """Generates random node values"""
        self.head = None 
        self.tail = None 
        for i in range(n):
            self.add(randint(min_value, maximum_value))

"""
custormLL = LinkedList()
custormLL.generate(10,0,99)
print(custormLL)
print(len(custormLL))
"""        