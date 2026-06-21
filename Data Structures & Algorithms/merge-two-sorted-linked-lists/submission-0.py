# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val < list2.val:
                new_val= list1.val
                list1 = list1.next
            else:
                new_val= list2.val
                list2 = list2.next
            head = ListNode(new_val)
            cur = head
            while list1 and list2:
                if list1.val < list2.val:
                    new_val= list1.val
                    list1 = list1.next
                else:
                    new_val= list2.val
                    list2 = list2.next
                cur.next = ListNode(new_val)
                cur = cur.next
            if list2:
                cur.next = list2
            else:
                cur.next = list1
            return head