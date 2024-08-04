from typing import Optional

class ListNode:
    """
    Definition for a singly-linked list node.
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    """
    Class containing the solution to remove duplicates from a sorted linked list.
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted linked list.

        :param head: The head node of the linked list.
        :return: The head node of the modified linked list.
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur = self._jump_duplicates(cur)
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next

    def _jump_duplicates(self, cur: ListNode) -> Optional[ListNode]:
        """
        Skip all duplicate nodes and return the first non-duplicate node.

        :param cur: The current node to start checking for duplicates.
        :return: The first non-duplicate node.
        """
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        return cur.next

