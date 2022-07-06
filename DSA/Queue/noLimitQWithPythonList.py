"""
    Here, we wanna create a Queue without size limit using Python List
"""


import queue


class Queue:
    def __init__(self):
        self.item_list = []


    def __str__(self):
        """This method prints the queue object when created"""
        #Use list comprehesnion
        values = [str(item) for item in self.item_list]
        return ' '.join(values)


    def isEmpty(self):
        """Returns true if the queue i empty. Otherwise False"""
        if self.item_list == []:
            return True 
        else:
            return False


    def enqueue(self, item):
        """Adds an item in the queue"""
        self.item_list.append(item)
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        """Removes the topmost element from the queue"""
        if self.isEmpty():
            return "The Queue is empty. No element to be dequeue"
        else:
            #return self.item_list.remove(self.item_list[0])
            return self.item_list.pop(0)


    def peek(self):
        """"Returns the topmost element in the Queue"""
        if self.isEmpty():
            return "The Queue is empty"
        else:
            return self.item_list[0]


    
    def delete(self):
        """"Delete the entire Queue"""
        self.item_list = None






queue = Queue()
print(queue.isEmpty())

for x in range(4):
    queue.enqueue(x)
print("peek: ", queue.peek())
print(queue)

print("'''''''''''''''''''''''''")
queue.dequeue()
print(queue)