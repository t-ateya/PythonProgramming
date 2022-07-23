class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
    def createList(self, arr):
        start = self.head
        n = len(arr)

        temp = start 
        i = 0
        while (i < n):
            newNode = Node(arr[i])
            if (i == 0):
                start = newNode
                temp = start 
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1

        self.head = start 
        return start 

    def printList(self):
        temp = self.head 
        linked_list = ""
        while (temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next 
        print(linked_list)

    def countList(self):
        temp = self.head 
        count = 0 
        while (temp):
            temp = temp.next 
            count +=1
        return count 

    #we will consider that the index starts at 1
    def insertAtLocation(self, value, index):
        temp = self.head 
        count = self.countList()


        if (count + 1 < index):
            return temp 

        newNode = Node(value)

        if (index == 1):
            newNode.next = temp 
            temp.prev = newNode
            self.head = newNode 
            return self.head

        if (index == count + 1):
            while (temp.next is not None):
                temp = temp.next 
            
            temp.next = newNode
            newNode.prev = temp 
            return self.head 

        i = 1
        while (i < index -1):
            temp = temp.next 
            i += 1

        nodeTarget = temp.next 
        newNode.next = nodeTarget
        nodeTarget.prev = newNode

        temp.next = newNode 
        newNode.prev = temp 

        return self.head 

    def deleteAtLocation(self, index):
        temp = self.head 
        count = self.countList()
        if (index > count ):
            return temp 
        
        if (index == 1):
            temp = temp.next 
            self.head = temp 
            return self.head 

        if (count == index):
            while (temp.next is not None and temp.next.next is not None):
                temp = temp.next 

            temp.next = None 
            return self.head 

        i = 1
        while (i < index - 1):
            temp = temp.next 
            i +=1

        prevNode = temp 
        nodeAtTarget = temp.next 
        nextNode = nodeAtTarget.next 


        nextNode.prev = prevNode
        prevNode.next = nextNode

        return self.head 



arr = [1,2,3,4,5]
llist = LinkedList()
llist.createList(arr)

llist.insertAtLocation(5,6)
llist.deleteAtLocation(2)
llist.printList()