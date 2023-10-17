from structures.priority_queue import PriorityQueue
from structures.stack import Stack
from utils.node import Node
from utils.path import get_path


def a_star(initial_state, goal_state):
    queue = PriorityQueue()
    initial_node = Node(initial_state)
    explored_states = Stack()
    explored_states.push(initial_node)
    visited_states = 0

    initial_node.set_searched()
    initial_node.set_depth(0)

    # set its heuristics as the sum of the actual heuristic and the cost (which is always one every tree layer)
    initial_node.set_heuristics(
        cost(heuristics(initial_node.state), initial_node.depth)
    )
    queue.enqueue(initial_node)  # add node to the queue

    print("Searching for a path...")
    # if the queue gets empty, no solution was found
    while len(queue.get_values()) > 0:
        print("queue: ", end="")
        [print(f"{e.__str__(True)} ", end="") for e in queue.get_values()]
        print()
        current_node = (
            queue.dequeue()
        )  # get the closest node according to its actual heuristics + cost
        visited_states += 1
        print(f"Depth: {current_node.depth}; current: {current_node.__str__(True)}")
        print()

        # check if goal was found
        if current_node.is_equal_to(goal_state):
            print("Goal found!")
            get_path(current_node)
            break

        # loop through current node possible actions
        edges = current_node.edges
        for e in edges:
            # check if the edge has been searched, is not on queue and if any similar state has been explored
            if (
                    not e.searched
                    and not queue.has_value(e)
                    and not explored_states.has_value(e)
            ):
                e.set_searched()
                e.set_depth(current_node.depth + 1)  # increment depth
                e.set_heuristics(cost(heuristics(e.state), e.depth))
                explored_states.push(e)
                e.parent = current_node  # set the parent
                queue.enqueue(e)


def cost(heuristics, depth):
    return heuristics + depth


def heuristics(state):
    # 6 - sum of M and C to make it admissible
    return 6 - (state.missionaries + state.cannibals)
