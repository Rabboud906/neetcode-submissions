class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Reverse the list
        new_head = self.reverseList(head)

        cursor = new_head
        prev = None
        x = 0

        # 2. Find nth node from beginning
        while cursor != None:
            if x == n - 1:
                # deleting first node
                if prev == None:
                    new_head = cursor.next
                else:
                    prev.next = cursor.next

                break

            prev = cursor
            cursor = cursor.next
            x += 1

        # 3. Reverse again
        return self.reverseList(new_head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current != None:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_

        return previous
