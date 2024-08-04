from typing import Optional, Tuple

class ListNode:
    """
    Class representing a node in a singly linked list.
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        """
        Initialize the ListNode.
        
        :param val: Value of the node.
        :param next: Reference to the next node in the list.
        """
        self.val = val
        self.next = next

class Solution:
    """
    Class containing the solution to reverse a segment of a linked list.
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse a segment of a singly linked list between positions left and right.

        :param head: The head node of the linked list.
        :param left: The starting position of the segment to be reversed.
        :param right: The ending position of the segment to be reversed.
        :return: The head node of the modified linked list.
        """
        # If the head is None or left is equal to right, no need to reverse.
        if not head or left == right:
            return head

        # Dummy node to handle edge cases where reversing includes the head.
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        prev_first = None
        first = None
        last = None
        next_last = None

        for i in range(1, right + 1):
            if left < i < right:
                # Reverse the pointers within the segment
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            else:
                if i == left:
                    # Mark the node before the start of the segment to be reversed
                    prev_first = prev
                    first = current
                elif i == right:
                    # Mark the node at the end of the segment to be reversed
                    next_last = current.next
                    current.next = prev
                    last = current
                
                # Move to the next node outside the segment
                current, prev = self._move_next(current, prev)

        if first:
            # Link the reversed segment to the node following the segment
            first.next = next_last

        if prev_first:
            # Link the node before the segment to the start of the reversed segment
            prev_first.next = last
        else:
            # If the head is part of the reversed segment
            dummy.next = last

        return dummy.next

    @staticmethod
    def _move_next(current: ListNode, prev: ListNode) -> Tuple[Optional[ListNode], ListNode]:
        """
        Helper function to move to the next node in the list.

        :param current: The current node.
        :param prev: The previous node.
        :return: A tuple containing the next node and the current node as the previous.
        """
        prev = current
        current = current.next
        return current, prev

