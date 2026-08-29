# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # 1. find the middle node
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        

        # 2. reverse the second hald mid -> none
        current = mid
        previous = None
        while current != None:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_

        # 3. merge them together 
        first = head
        second = previous

        while first is not None and second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        