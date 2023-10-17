from typing import List

from utils.node import Node


class Stack:
    """Stack data structure for DFS"""

    def __init__(self):
        self.values: List[Node] = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def get_values(self):
        return self.values

    def has_value(self, node):
        for value in self.values:
            if value.state.is_equal_to(node.state):
                return True
        return False
