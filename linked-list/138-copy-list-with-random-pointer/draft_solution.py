"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        nodePosMap = self.getNodePosMap(head)
        posRanPosMap = self.getPosRanPosMap(head, nodePosMap)
       
        cur = head.next
        copyHead = Node(head.val)
        copyCur = copyHead

        while cur:
            nextNode = Node(cur.val)
            copyCur.next = nextNode
            copyCur = nextNode
            cur = cur.next

        posNodeMap = self.getPosNodeMap(copyHead)
        cur = copyHead
        i = 0

        while cur:
            if posRanPosMap[i] is not None:
                cur.random =  posNodeMap[posRanPosMap[i]]
            else:
                cur.random = None

            i+=1
            cur = cur.next

        return copyHead

    
    def getNodePosMap(self, head):
        cur = head
        nodePosMap = {}
        i = 0

        while cur:
            nodePosMap[cur] = i
            i+=1
            cur = cur.next
        
        return nodePosMap

    def getPosRanPosMap(self, head, nodePosMap):
        cur = head
        posRanPosMap = {}
        i = 0

        while cur:
            posRanPosMap[i] =  None if cur.random is None else nodePosMap[cur.random]
            cur = cur.next
            i+=1

        return posRanPosMap
    
    def getPosNodeMap(self, head):
        cur = head
        posNodeMap = {}
        i = 0

        while cur:
            posNodeMap[i] = cur
            i+=1
            cur = cur.next
        
        return posNodeMap
