"""
    Medium #328
    Odd Even LinkedList

    Given a singly linked list, group all odd nodes together followed by the even nodes.
    Note: We're talking about the number and not the value in the nodes.
"""
class ListNode:
    def __init__(self, data) -> None:
        self.value = data
        self.next = None 

class Solution:
    def oddEvenList(self, head:ListNode)->ListNode:
        """Returns a new list with odd nodes followed by even nodes"""
        if (not head):
            return head 
        
        odd = head 
        even = odd.next 
        even_list = even 

        while (even and even.next):
            odd.next = even.next 
            odd = odd.next 

            even.next = odd.next 
            even = even.next

        odd.next = even_list
        return head 

node_10 = ListNode(10)
node_20 = ListNode(20)
node_30 = ListNode(30)
node_40 = ListNode(40)
node_50 = ListNode(50)

node_10.next = node_20
node_20.next = node_30
node_30.next = node_40
node_40.next = node_50

s = Solution()
head = s.oddEvenList(node_10)

while(head):
    print(head.value)
    head = head.next 