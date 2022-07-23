"""
    -Medium #2
    You're given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of the nodes contain a single digit. 
    Add the two numbers and return it as a linked list.
"""
class ListNode:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)->ListNode:
        ans = ListNode(None)
        pointer:ListNode = ans 
        carry:int = 0
        sum :int = 0

        while (l1 is not None or l2 != None):
            sum = carry 
            if (l1):
                sum += l1.value
                l1 = l1.next
            if (l2 != None):
                sum += l2.value
                l2 = l2.next 

            carry = sum//10 #Same as int(sum/10)
            pointer.next = ListNode(sum%10)
            pointer = pointer.next 

            if (carry > 0):
                pointer.next = ListNode(carry)

        return ans.next

s = Solution()

l1_node_2 = ListNode(2)
l1_node_4 = ListNode(4)
l1_node_3 = ListNode(3)

l1_node_2.next = l1_node_4
l1_node_4.next = l1_node_3

l2_node_5 = ListNode(5)
l2_node_6 = ListNode(6)
l2_node_4 = ListNode(4)

l2_node_5.next = l2_node_6
l2_node_6.next = l2_node_4

ans = s.addTwoNumbers(l1_node_2, l2_node_5)

while (ans):
    print(ans.value)
    ans = ans.next


