class Node:
    def __init__(self, value =None):
        self.data = value 
        self.next = None


class SLinkedList:
    #None == Null
    def __init__(self):
        self.head = None
        self.tail = None 


singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
#singlyLinkedList.head.next == node1.next
node1.next = node2
singlyLinkedList.tail = node2
