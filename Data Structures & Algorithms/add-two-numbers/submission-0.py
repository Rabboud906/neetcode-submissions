# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#10 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        h = ListNode(0)
        cursor = h
        carry_out = 0
        while cur_l1 or cur_l2:
            val1 = cur_l1.val if cur_l1 else 0
            val2 = cur_l2.val if cur_l2 else 0
            s = val1 + val2 + carry_out 
            carry_out = s//10
            s_out = s %10
            new_Node = ListNode(s_out)
            cursor.next = new_Node
            cursor = cursor.next
            if cur_l1:
                cur_l1 = cur_l1.next
            if cur_l2:
                cur_l2 = cur_l2.next
        if carry_out:
            cursor.next = ListNode(carry_out)
        return h.next
