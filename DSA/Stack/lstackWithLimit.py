
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []


    def __str__(self):
        values = self.list.reverse()
        values  = [str(value) for value in self.list]
        return '\n'.join(values)


    def isEmpty(self):
        """Returns True if the stack is empty and False otherwise"""
        if len(self.list) == 0: 
            return True 
        else:
            return False


    def isFull(self):
        """Checks if the stack is full and returns True. Otherwise False"""
        if len(self.list) == self.max_size:
            return True
        else:
            return False


    def push(self, item):
        """Adds an element to the stack"""
        if self.isFull():
            return "The stack is full. Can't push more items"
        else:
            self.list.append(item)
            return "The element has been successfully inserted"

    
    def pop(self):
        """returns the top element from the stack"""
        if self.isEmpty():
            return "There's no element in the stack"
        else:
            return self.list.pop()



    def peek(self):
        """Returns the last element in the stack"""
        if self.isEmpty():
            return "There's no element in the stack"
        else:
            return self.list[len(self.list) -1]


    def delete_stack(self):
        """Method deletes the emtire stack"""
        self.list = None


    







            
customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)

print(customStack.isFull())

print(customStack)