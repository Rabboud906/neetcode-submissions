class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current != None:
            next_ = current.next
            current.next = previous
            previous = current 
            current = next_
        return previous






