MAX_MISSIONARIES = 3
MAX_CANNIBALS = 3


class State:
    """Represents a single state of the Missionary and Cannibal problem"""

    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.actions = self.get_state_possible_actions()

    def has_more_cannibals_on_left_bank(self):
        """Check if Cannibals outnumber Missionaries on the left bank"""
        return ((self.missionaries == 2 and self.cannibals == 1) or
                (self.missionaries == 1 and self.cannibals == 0) or
                (self.missionaries == 2 and self.cannibals == 0))

    def has_more_cannibals_on_right_bank(self):
        """Check if Cannibals outnumber Missionaries on the right bank"""
        return ((self.missionaries == 1 and self.cannibals == 3) or
                (self.missionaries == 2 and self.cannibals == 3) or
                (self.missionaries == 1 and self.cannibals == 2))

    def is_valid(self):
        """Check if the current state is valid"""

        # check if the number of Missionaries or Cannibals outnumber its limit
        if self.missionaries > MAX_MISSIONARIES or self.missionaries < 0:
            return False
        if self.cannibals > MAX_CANNIBALS or self.cannibals < 0:
            return False

        # Check if there are more Cannibals than Missionaries at any side
        if self.has_more_cannibals_on_left_bank():
            return False
        if self.has_more_cannibals_on_right_bank():
            return False

        return True

    @staticmethod
    def get_all_possible_actions():
        """List all possible moves on the problem"""
        return [
            [2, 0],  # move: Two missionaries, no cannibals
            [1, 0],  # move: One missionary, no cannibals
            [1, 1],  # move: One missionary, one cannibal
            [0, 1],  # move: No missionaries, one cannibal
            [0, 2]  # move: No missionaries, two cannibals
        ]

    def get_state_possible_actions(self):
        """Get all possible actions and filter depending on the number of missionaries and cannibals, and boat's
        direction"""

        # fetching all possible actions
        all_actions = self.get_all_possible_actions()
        actions = []

        # If the number of M or C on the right bank (number represented by state)
        # is greater than the current action, the algo keeps it
        if self.is_boat_on_right_bank():
            for action in all_actions:
                if self.missionaries >= action[0] and self.cannibals >= action[1]:
                    action.append(not self.is_boat_on_right_bank())
                    actions.append(action)

        # Subtract the number of M and C by three (max limit of M and C)
        # to get the number of M and C on the left bank of the river
        else:
            for action in all_actions:
                if ((MAX_MISSIONARIES - self.missionaries >= action[0]) and
                        (MAX_CANNIBALS - self.cannibals >= action[1])):
                    action.append(not self.is_boat_on_right_bank())
                    actions.append(action)

        return actions

    def is_boat_on_right_bank(self):
        """This method checks and returns if the boat is currently on the right bank"""
        return self.boat

    def is_equal_to(self, state):
        if self.missionaries != state.missionaries:
            return False

        if self.cannibals != state.cannibals:
            return False

        if self.boat != state.boat:
            return False

        return True

    def __str__(self, heuristics) -> str:
        return f'({self.missionaries}, {self.cannibals}, {self.boat}, {heuristics})' if heuristics \
            else f'({self.missionaries}, {self.cannibals}, {self.boat})'
