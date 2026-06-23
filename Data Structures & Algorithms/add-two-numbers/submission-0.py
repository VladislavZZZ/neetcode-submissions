# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        n1 = 0
        i = 1
        while cur:
            n1+=cur.val*i
            i*=10
            cur = cur.next
        n2 = 0
        cur = l2
        i = 1
        while cur:
            n2+=cur.val*i
            i*=10
            cur = cur.next
        
        n3 = n2+n1
        res = ListNode(n3%10)
        n3//=10
        cur = res
        while n3>0:
            cur.next = ListNode(n3%10)
            n3//=10
            cur = cur.next
        return res