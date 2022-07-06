
from LinkedList import LinkedList
 

"""
    Q1.Write code to remove duplicates from an unsorted linked list
"""

"""
    Q2.
    Return Nth to Last
    Implement an algorith to find the nth to last element of SLL
"""

def remove_duplicate(unsortedLL):
    """The method removes duplicate elements from an unsorted LL"""
    if unsortedLL.head is None:
        return 
    else:
        tempNode = unsortedLL.head 
        tempList = []
        while tempNode:
            tempList.append(unsortedLL.value)
            if unsortedLL.value in tempList:
                continue
            tempNode = tempNode.next 
        return tempList

def removeDups(ll):
    """Instructor's method"""
    if ll.head is None:
        return 
    else:
        currentNode = ll.head 
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
    return ll


def removeDups1(ll):
    """Removes duplicate elements without using a set buffer"""
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head


def returnNthElementFromLast(ll, N):
    """This method returns N to last element in a singly linked List"""
    if ll.head  == None:
        return 
    else:
        tempNode = ll.head
        index = 0
        while index < (len(ll)-N):
            tempNode = tempNode.next
            index +=1
        return tempNode.value


def nthToLast(ll,n):
    """Developed by the instructor"""
    pointer1 = ll.head
    pointer2 = ll.head 

    for i in range(n):
        if pointer2 is None:
            return None 
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next 
    return pointer1


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(returnNthElementFromLast(customLL,3 ))
print(nthToLast(customLL,3))