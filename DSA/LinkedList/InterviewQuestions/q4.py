from unittest import result
from LinkedList import LinkedList


"""
        Q4. Sum Lists
        You have two numbers represented by a linked list, where each node contains a single digit.
        The digits are stored in reverse order, such that the 1's digit is at the head of the list.
        Write a function that adds the two numbers and returns the sum as a linked list

"""

def sumLists(ll1, ll2):
    """Returns the sum of two digits of a linked list stored in reverse order. My solution"""
    list1 = []
    list2 = []
    pointer1 = ll1.head 
    pointer2 = ll2.head 
    while pointer1:
        list1.append(pointer1.value)
        pointer1 = pointer1.next

    while pointer2:
        list2.append(pointer2.value)
        pointer2 = pointer2.next

    list1.reverse()
    list2.reverse()

    index1 = len(list1) -1
    
    newList = []
    carry = 0
    while index1 >=0:
        sum = list1[index1] + list2[index1] + carry
        if sum >10:
            carry =1
            sum = sum %10   
    
        newList.append(sum)
        index1 -=1
        
    #newList.reverse()
    newLL = LinkedList()
    for i in range(len(newList)):
        newLL.add(newList[i])
    
    return newLL

def sumLists2(llA, llB):
    """Tutor's solution"""
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next 
        if n2:
            result += n2.value 
            n2 = n2.next
        ll.add(int(result % 10))   
        carry = result / 10
    return ll
    







ll1 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)

ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)

print(ll1)
print(ll2)
print(sumLists(ll1,ll2))
print(sumLists2(ll1,ll2))

