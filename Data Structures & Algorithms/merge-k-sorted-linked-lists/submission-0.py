# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self,node) -> None:
        self.node = node
    
    def __lt__(self, other):
        return self.node.val<other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        dummy = ListNode()
        cur = dummy
        minHeap = []

        for lst in lists:
            if lst:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        while minHeap:
            cur_node = heapq.heappop(minHeap)
            cur.next = cur_node.node
            cur = cur.next

            if cur_node.node.next:
                heapq.heappush(minHeap, NodeWrapper(cur_node.node.next))

        return dummy.next