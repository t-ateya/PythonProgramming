
class Stack:
    def __init__(self):
        self.list = []


    """
    """
    def __str__(self):
        values = self.list.reverse()
        values  = [str(value) for value in self.list]
        return '\n'.join(values)


    #isEmpty
    def isEmpty(self):
        """Returns True if the stack is empty. Otherwise false"""
        if self.list == []:
            return True
        else:
            return False


    def push(self, value):
        """Pushes an element into the stack"""
        self.list.append(value)
        return "The element has been successfully inserted"


    def pop(self):
        """returns the top element from the stack"""
        if self.isEmpty():
            return "There's no element in the stack"
        else:
            return self.list.pop()

    

    def peak(self):
        """Returns the last element in the stack"""
        if self.isEmpty():
            return "There's no element in the stack"
        else:
            return self.list[len(self.list) -1]

    
    def delete(self):
        """This  method deletes the entire stack"""
        self.list = None






stack = Stack()
"""
stack.list.append(1)
stack.list.append(2)
stack.list.append(3)
stack.list.append(4)
stack.list.append(5)
stack.list.append(6)
"""



#[stack.push(x) for x in range(1,4)]

stack.push(1)
stack.push(2)
stack.push(3)

print("peak: ",stack.peak())

print(stack)


