# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode()
        dummy.next = head
        prevGr = dummy
        while True:
            last_in_group = self.getLastInGroup(prevGr, k)
            if not last_in_group:
                break
            groupNext = last_in_group.next
            cur, prev = prevGr.next, last_in_group.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = prevGr.next
            prevGr.next = last_in_group
            prevGr = tmp
        return dummy.next    

    def getLastInGroup(self,cur, k):
        while cur and k>0:
            cur = cur.next
            k-=1
        return cur