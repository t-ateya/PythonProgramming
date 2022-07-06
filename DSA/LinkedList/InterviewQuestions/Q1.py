from LinkedList import LinkedList


"""
    Q1.Write code to remove duplicates from an unsorted linked list
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


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
#removeDups(customLL)
removeDups1(customLL)
print(customLL)