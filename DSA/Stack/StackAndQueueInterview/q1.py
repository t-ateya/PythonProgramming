"""
    q1. Three in One
    Describe how you  could use a single Python list to implement three stacks
"""

from threading import stack_size


class MultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.number_of_stacks = 3
        self.custom_list = [0]*(stack_size*self.number_of_stacks)
        self.sizes = [0]*self.number_of_stacks

    
    def isFull(self, stack_number):
        """"Returns the True if the stack is full and False otherswise"""
        if self.sizes[stack_number] == self.stack_size:
            return True 
        else:
            return False


    def isEmpty(self, stack_number):
        """Returns True if the stack is empty and False otherwise"""
        if self.sizes[stack_number] == 0:
            return True 
        else:
            False 


    def indexOfTop(self, stacknum):
        offset = stacknum*self.stack_size
        return offset + self.sizes[stacknum]


    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "Stack is Full"
        else:
            self.sizes[stacknum] +=1
            self.custom_list[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        """Removes an element from the top of the stack"""
        if self.isEmpty(stacknum):
            return "The stack is Empty"
        else:
            value = self.custom_list[self.indexOfTop(stacknum)]
            self.custom_list[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        """"Returns the topmost element in the stack"""
        if self.isEmpty(stacknum):
            return "The stack is Empty"
        else:
            return self.custom_list[self.indexOfTop(stacknum)]



customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.peek(2))