"""
    #141
    Given a linked list, return a boolean indicating if there is a cycle.
"""
class ListNode:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Solution:
    def hasCycle(self, head: ListNode)->bool:
        hare = head 
        turtle = head 

        while (turtle and hare and hare.next):
            hare = hare.next.next 
            turtle = turtle.next

            if (turtle == hare):
                return True 
        return False

s = Solution()

node_1 = ListNode(1)
node_5 = ListNode(5)
node_11 = ListNode(11)
node_8 = ListNode(8)
node_9 = ListNode(9)

node_1.next = node_5
node_5.next = node_11
node_11.next = node_8
node_8.next = node_9
#node_9.next = node_5

print(s.hasCycle(node_1))

