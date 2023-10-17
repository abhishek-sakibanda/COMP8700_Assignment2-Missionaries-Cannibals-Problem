from algorithms.a_star import a_star
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.gfs import greedy_bfs
from utils.state import State


def main():
    print("Select an Algorithm:")
    print("\t1. Breadth-first Search")
    print("\t2. Depth-first Search")
    print("\t3. Greedy Best-first Search")
    print("\t4. A-star Search")
    choice = int(input("Please choose an option: "))

    INITIAL_STATE_TUPLE = State(0, 0, False)
    GOAL_STATE_TUPLE = State(3, 3, True)

    if choice == 1:
        bfs(INITIAL_STATE_TUPLE, GOAL_STATE_TUPLE)

    elif choice == 2:
        dfs(INITIAL_STATE_TUPLE, GOAL_STATE_TUPLE)

    elif choice == 3:
        greedy_bfs(INITIAL_STATE_TUPLE, GOAL_STATE_TUPLE)

    elif choice == 4:
        a_star(INITIAL_STATE_TUPLE, GOAL_STATE_TUPLE)

    else:
        pass


if __name__ == "__main__":
    main()
