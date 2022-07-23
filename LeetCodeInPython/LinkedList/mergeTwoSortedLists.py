"""
#Easy 21
    Given 2 separated sorted linked lists, merge them together and return the sorting
"""
class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None 
        

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        curr = ListNode(0)
        ans = curr

        while (l1 and l2):
            if (l1.value > l2.value):
                curr.next = l2
                l2 = l2.next 
            else:
                curr.next = l1
                l1 = l1.next 
            curr = curr.next 
        
        while (l1):
            curr.next = l1 
            l1 = l1.next 
            curr = curr.next 

        while (l2):
            curr.next = l2
            l2 = l2.next 
            curr = curr.next 
        
        return ans.next 

s = Solution()
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_4 = ListNode(4)

l1_1.next = l1_2
l1_2.next = l1_4

l2_1 = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)

l2_1.next = l2_3
l2_3.next = l2_4

ans = s.mergeTwoLists(l1_1, l2_1)
print(ans)

while (ans):
    print(ans.value)
    ans = ans.next



