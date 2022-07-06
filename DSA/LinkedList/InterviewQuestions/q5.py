

from LinkedList import LinkedList, Node
"""
    Q5. Intersection
    Given two (singly) linked Lists, determine if the two lists intersect. Return the intersection node.
    Note that the intersection is defined based on reference, not value. That is, if the kth node of the 
    linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting

"""

def intersection(ll1, ll2):
    """Determines if two singly linked lists intersect and returns the intersection value"""
    
    index = 0
    len_diff = len(ll1) - len(ll2)
    
    if len_diff > 0:
        while index < len_diff:
            ll1.head = ll1.head.next
            index += 1
    elif len_diff < 0:
        while index < abs(len_diff):
            ll2.head = ll2.head.next 
            index +=1 
    node1 = ll1.head 
    node2 = ll2.head 
    
    while node1:
       # print(node1.value)
        print(node2.value)
        node1 = node1.next 
        node2 = node2.next 
        if node1 == node2:
            return f"node returned: {node1}"
    
    

def intersection2(llA, llB):
    """Professor's approach"""
    #1. Check if the nodes intersect or not. The nodes intersect they both reference the same tail
    #NB. Use llA.tail.value == llB.tail.value when checking for values and llA.tail is llB.tail when checking for ref
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head 

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next 
        longerNode = longerNode.next
    
    return longerNode


#Helper addition method
def addSameNode(llA, llB, value):
    """Adds same node at the end of both llA and llB"""
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

    


llA  = LinkedList() 
llA.generate(3, 0, 10)

llB  = LinkedList()      
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection2(llA, llB))

"""
ll1.add(3)
ll1.add(1)
ll1.add(5)
ll1.add(9)
ll1.add(7)
ll1.add(2)
ll1.add(1)

ll2.add(2)
ll2.add(4)
ll2.add(6)
ll2.add(7)
ll2.add(2)
ll2.add(1)

print(ll1)
print(ll2)
print(intersection(ll1,ll2))
"""






        
        