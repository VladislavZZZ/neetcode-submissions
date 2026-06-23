"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map_for_copy = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            map_for_copy[cur] = copy
            cur= cur.next

        cur = head
        while cur:
            copy = map_for_copy[cur]
            copy.next = map_for_copy[cur.next]
            copy.random = map_for_copy[cur.random]
            cur= cur.next
        
        return map_for_copy[head]