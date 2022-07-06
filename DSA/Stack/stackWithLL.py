class Node:
    def __init__(self,value ):
        self.value = value 
        self.next = None 




class LinkedList:
    def __init__(self):
        self.head = None 

    def __iter__(self):
        currentNode = self.head 
        while currentNode:
            yield currentNode
            currentNode = currentNode.next 



class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
    

    def __str__(self):
        values = [str(item.value) for item in self.linkedList]
        return '\n'.join(values)


    def isEmpty(self):
        """Checks if the LinkedList is empty or not"""
        if self.linkedList.head == None:
            return True 
        else:
            return False

    def push(self, item):
        """"Pushes and item to a stack"""
        newNode = Node(item)
        newNode.next = self.linkedList.head
        self.linkedList.head = newNode

    
    def pop(self):
        """Returns the first element in the stack"""
        if self.isEmpty():
            return "There is no element in the stack to remove"
        else:
            tempNode = self.linkedList.head
            self.linkedList.head = tempNode.next 
            return tempNode.value


    def peek(self):
        """"Returns the topmost value in the stack"""
        if self.isEmpty():
            return "There is no element in the stack to remove"
        else: 
            return self.linkedList.head.value


    def delete(self):
        """Deletes the entire stack"""
        if self.isEmpty():
            return "The stack is empty. No elements to be deleted"
        else:
            self.linkedList.head = None 








stack = Stack()

for x in range(4):
    stack.push(x)

print(stack)

print("peak: ",stack.peak())
print(stack.pop())
print("========================")
print("peak: ",stack.peak())

print(stack)