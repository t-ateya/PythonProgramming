"""
    medium #19
    Remove the Nth node from the end of list.

    Given a linked list, remove the n-th node from the end of list and return its head.
"""

class ListNode:
    def __init__(self, data, next = None) -> None:
        self.val = data
        self.next = next


class Solution:
    def removeNthFromEnd(self, head:ListNode, n:int)->ListNode:
        ans:ListNode = ListNode(0)
        ans.next = head 

        first = ans 
        second = ans 

        for i in range(1, n+2):
            first = first.next

        while (first is not None):
            first = first.next 
            second = second.next

        second.next = second.next.next

        return ans.next


sol = Solution()
node_1 = ListNode(1)
node_3 = ListNode(3)
node_5 = ListNode(5)
node_7 = ListNode(7)

node_1.next = node_3
node_3.next = node_5
node_5.next = node_7

head = sol.removeNthFromEnd(node_1, 2)

while(head):
    print(head.val)
    head= head.next