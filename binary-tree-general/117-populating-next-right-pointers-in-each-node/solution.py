class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        prev = None
        
        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.pop(0)

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

