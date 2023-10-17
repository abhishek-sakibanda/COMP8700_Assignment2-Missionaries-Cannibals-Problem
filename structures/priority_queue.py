from typing import List

from utils.node import Node


class PriorityQueue:
    def __init__(self):
        self.values: List[Node] = []

    def get_values(self) -> List[Node]:
        return self.values

    def enqueue(self, value: Node):
        self.values.append(value)

    def dequeue(self):
        min_value: int = 999
        index: int = -1
        for value in self.values:
            if value.heuristic_value < min_value:
                min_value = value.heuristic_value
                index = self.values.index(value)

        return self.values.pop(index)

    def has_value(self, node: Node):
        for value in self.values:
            if value.state.is_equal_to(node.state):
                return True

        return False
