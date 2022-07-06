"""Write a program to partition a Linked List from a given value x

    Q3. Partition
    Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
"""

from LinkedList import LinkedList

def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head 

    while curNode:
        nextNode = curNode.next 
        curNode.next = None 
        if curNode.value < x:
            curNode.next = ll.head 
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode

    if ll.tail.next != None:
        ll.tail.next = None 


customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 45)
print(customLL)


