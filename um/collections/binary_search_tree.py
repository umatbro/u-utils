from typing import Union, Any
from queue import Queue


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def breadth_first_search(self, value: Any) -> Union['Node', None]:
        """
        Search node children using breadth-first search.

        :param value: searched value
        :return: reference to the node containing searched value or None if value not found
        """
        if self.value == value:
            return self

        if self.right is None and self.left is None:
            return None

        nodes_to_search = Queue()

        if self.right is not None:
            nodes_to_search.put(self.right)
        if self.left is not None:
            nodes_to_search.put(self.left)

        while not nodes_to_search.empty():
            node = nodes_to_search.get()

            if node.value == value:
                return node

            if node.right is not None:
                nodes_to_search.put(node.right)
            if node.left is not None:
                nodes_to_search.put(node.left)

    def depth_first_search(self, value: Any) -> Union['Node', None]:
        if self.value == value:
            return self

        if self.left is not None:
            left_result = self.left.depth_first_search(value)
            if left_result is not None:
                return left_result

        if self.right is not None:
            right_result = self.right.depth_first_search(value)
            if right_result is not None:
                return right_result

        return None

# root = Node(1)
# root.left = Node(21)
# root.left.left = Node(31)
# root.right = Node(3)
# root.right.left = Node(2)
# print(root.depth_first_search(1))