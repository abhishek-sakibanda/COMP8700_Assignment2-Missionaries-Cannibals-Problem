from typing import List

from utils.state import State


class Node:
    """Represents a node to store a state and other values"""

    def __init__(self, state: State):
        self.state: State = state
        self.edges: List[Node] = []
        self.searched: bool = False
        self.parent = None
        self.heuristic_value = None
        self.depth = None

    def set_searched(self):
        self.searched = True
        self.calculate_edges()

    def set_heuristics(self, value):
        self.heuristic_value = value

    def set_depth(self, value):
        self.depth = value

    def is_equal_to(self, goal) -> bool:
        return self.state.is_equal_to(goal)

    def calculate_edges(self):
        for action in self.state.actions:
            # if the boat is going to goal state
            if action[2]:
                new_node = Node(
                    State(
                        missionaries=self.state.missionaries + action[0],
                        cannibals=self.state.cannibals + action[1],
                        boat=action[2]
                    )
                )
                if new_node.state.is_valid():
                    self.edges.append(new_node)

            else:
                new_node = Node(
                    State(
                        missionaries=self.state.missionaries - action[0],
                        cannibals=self.state.cannibals - action[1],
                        boat=action[2]
                    )
                )
                if new_node.state.is_valid():
                    self.edges.append(new_node)

    def __str__(self, show_heuristic=False) -> str:
        return f'{self.state.__str__(self.heuristic_value)}' if show_heuristic else f'{self.state.__str__(None)}'
