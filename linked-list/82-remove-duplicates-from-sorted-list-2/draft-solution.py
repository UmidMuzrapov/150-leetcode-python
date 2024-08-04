# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None

        cur = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while cur and cur.next:
            if cur.val == cur.next.val:
                then = self.jumpDiplicates(cur)
                prev.next = then
                cur = then
            else:
                prev = cur
                cur = cur.next
        
        return dummy.next
        
    def jumpDiplicates(self, cur):
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        
        return cur.next
