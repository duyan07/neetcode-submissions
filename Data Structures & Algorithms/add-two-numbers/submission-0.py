# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_lists(a, b, carry=0):
            if not a and not b:
                if carry == 0:
                    return None
                else:
                    return ListNode(carry)
            
            v1 = a.val if a else 0
            v2 = b.val if b else 0
            res = v1 + v2 + carry
            digit = ListNode(res % 10)
            carry = res // 10

            if a and b:
                digit.next = add_lists(a.next, b.next, carry)
            elif a and not b:
                digit.next = add_lists(a.next, b, carry)
            else:
                digit.next = add_lists(a, b.next, carry)
            
            return digit
        
        return add_lists(l1, l2)