"""
    Q4. Queue via Stacks

    Implement Queue class which implements a queue using two stacks
"""

class Stack():
    def __init__(self):
        self.list = []

    
    def __len__(self):
        return len(self.list)
    

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None 
        return self.list.pop()


class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        firstElement=self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return firstElement



customQ = QueueViaStack()
for i in range(1,4):
    customQ.enqueue(i)

print(customQ.dequeue())
customQ.enqueue(6)
print(customQ.dequeue())