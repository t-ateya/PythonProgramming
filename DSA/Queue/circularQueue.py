"""Creating a Queque with fixed size"""

from sys import maxsize


class Queue:
    def __init__(self, maxSize):
        self.items = maxSize*[None] #set all the items to None
        self.maxSize = maxSize
        self.start = -1
        self.top = -1


    def __str__(self):
        values = [str(item) for item in self.items]
        return ' '.join(values)


    def isFull(self):
        """Checks if the Queue is full"""
        if self.top + 1 == self.start:
            return True 
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    

    def enqueue(self, value):
        """Adds a new item to a queue"""
        if self.isFull():
            return f"The queue is full. Can't insert {value}"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start +=1
            self.items[self.top] = value 
            return "The element is inserted at the end of Queue"

    
    def dequeue(self):
        """Removes an element from a Queue"""
        if self.isEmpty():
            return "The Queue is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start +=1
            self.items[start] = None 
            return firstElement


    def peek(self):
        """Returns the first element in the Queue"""
        if self.isEmpty():
            return "The Queue is empty"
        else:
            return self.items[self.start]


    
    def delete(self):
        """Delete all elements from the Queue"""
        if self.isEmpty():
            return "The Queue is empty."
        else:
            self.start = -1
            self.top = -1
            self.items = self.maxSize*[None]

            




customQueue = Queue(3)


customQueue.enqueue(2)
customQueue.enqueue(4)
customQueue.enqueue(6)
#print(customQueue.enqueue(7))
#print(customQueue.isEmpty())
print(customQueue)

print(customQueue.delete())


"""
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
"""
print(customQueue)

