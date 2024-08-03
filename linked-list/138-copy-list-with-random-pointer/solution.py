from typing import Optional, Dict

class Node:
    """A node in a linked list with a random pointer."""
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val: int = int(x)
        self.next: Optional['Node'] = next
        self.random: Optional['Node'] = random

class Solution:
    """Solution for copying a linked list with random pointers."""
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Create a deep copy of the given linked list with random pointers.
        This function orchestrates the entire copying process using helper methods.
        """
        if not head:
            return None
        
        node_to_position = self._create_node_to_position_map(head)
        position_to_random_position = self._create_position_to_random_position_map(head, node_to_position)
        new_head = self._create_new_list(head)
        position_to_new_node = self._create_position_to_node_map(new_head)
        self._set_random_pointers(new_head, position_to_random_position, position_to_new_node)
        
        return new_head

    def _create_node_to_position_map(self, head: Node) -> Dict[Node, int]:
        """
        Creates a mapping of original nodes to their positions in the list.
        This helps in quickly identifying the position of a node.
        """
        node_to_position = {}
        current = head
        position = 0
        while current:
            node_to_position[current] = position
            current = current.next
            position += 1
        return node_to_position

    def _create_position_to_random_position_map(self, head: Node, node_to_position: Dict[Node, int]) -> Dict[int, Optional[int]]:
        """
        Creates a mapping of node positions to the positions of their random pointers.
        This helps in setting up random pointers in the copied list later.
        """
        position_to_random_position = {}
        current = head
        position = 0
        while current:
            position_to_random_position[position] = (
                node_to_position[current.random] if current.random else None
            )
            current = current.next
            position += 1
        return position_to_random_position

    def _create_new_list(self, head: Node) -> Node:
        """
        Creates a new list by copying the values from the original list.
        This new list doesn't have random pointers set yet.
        """
        new_head = Node(head.val)
        current_new = new_head
        current_old = head.next
        while current_old:
            current_new.next = Node(current_old.val)
            current_new = current_new.next
            current_old = current_old.next
        return new_head

    def _create_position_to_node_map(self, head: Node) -> Dict[int, Node]:
        """
        Creates a mapping of positions to nodes in the new list.
        This helps in quickly accessing nodes by their position when setting random pointers.
        """
        position_to_node = {}
        current = head
        position = 0
        while current:
            position_to_node[position] = current
            current = current.next
            position += 1
        return position_to_node

    def _set_random_pointers(self, head: Node, position_to_random_position: Dict[int, Optional[int]], position_to_new_node: Dict[int, Node]) -> None:
        """
        Sets the random pointers in the new list based on the mappings created earlier.
        This completes the deep copy of the original list.
        """
        current = head
        position = 0
        while current:
            random_position = position_to_random_position.get(position)
            current.random = position_to_new_node.get(random_position) if random_position is not None else None
            current = current.next
            position += 1
