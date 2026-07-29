# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        c1 = list1
        c2 = list2

        while c1 and c2:
            if c1.val <= c2.val:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next
        
        if c1 and not c2:
            curr.next = c1
        elif not c1 and c2:
            curr.next = c2
            
        return res.next