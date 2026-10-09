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
        if not head: return None

        adds = {None: None}
        dummy = Node(0)
        curr = dummy
        i = head
        while i:
            new_node = Node(i.val)
            adds[i] = new_node
            curr.next = new_node
            curr = curr.next
            i = i.next
        
        i = head
        while i:
            adds[i].random = adds[i.random]
            i = i.next
        
        return dummy.next