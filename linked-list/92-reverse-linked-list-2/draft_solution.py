class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        current = head
        prev_first = None
        first = None
        last = None
        next_last = None

        for i in range(1, right + 1):
            if left < i < right:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            else:
                if i == left:
                    prev_first = prev
                    first = current
                elif i == right:
                    next_last = current.next
                    current.next = prev
                    last = current

                current, prev = self._move_next(current, prev)

        if first:
            first.next = next_last

        if prev_first:
            prev_first.next = last
        else:
            dummy.next = last

        return dummy.next

    @staticmethod
    def _move_next(current: ListNode, prev: ListNode) -> Tuple[Optional[ListNode], ListNode]:
        prev = current
        current = current.next
        return current, prev
