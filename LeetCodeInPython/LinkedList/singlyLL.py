import ssl


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 



class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def print_list(self):
        temp = self.head 
        linked_list = ""
        while (temp):
            linked_list += str(temp.data) + "=>"
            temp = temp.next 
        print(linked_list)

    def insertNode(self, val, pos):
        target = Node(val)
        if (pos == 0):
            target.next = self.head 
            self.head = target 
            return 

        def getPrev(pos):
            temp = self.head 
            count = 1
            while(count < pos):
                temp = temp.next
                count +=1
            return temp 

        prev = getPrev(pos)
        nextNode = prev.next

        prev.next = target 
        target.next = nextNode





singly_linked_list = LinkedList()
node1 = Node(1)
node2 = Node(5)
node3 = Node(3)
node4 = Node(7)

singly_linked_list.head = node1 
node1.next = node2
node2.next = node3
node3.next = node4

singly_linked_list.print_list()

singly_linked_list.insertNode(2,4)
singly_linked_list.print_list()

