"""
Name:Shanie Portal
Date:01/28/24
Assignment:Module3: Implement Search
Due Date:01/28/24
About this project: This program solves the farmer, wolf, goat, cabbage riddle.
Assumptions:No assumptions are made.
All work below was performed by Shanie Portal (Inspired by Dr. Works' example video on missionaries & cannibals)
"""

class State():
    def __init__(self, farmerLeft, wolfLeft, goatLeft, cabbageLeft, boat, farmerRight, wolfRight, goatRight,
                 cabbageRight):
        self.farmerLeft = farmerLeft
        self.wolfLeft = wolfLeft
        self.goatLeft = goatLeft
        self.cabbageLeft = cabbageLeft
        self.boat = boat
        self.farmerRight = farmerRight
        self.wolfRight = wolfRight
        self.goatRight = goatRight
        self.cabbageRight = cabbageRight
        self.parent = None

    def is_goal(self):
        if self.farmerLeft == 0 and self.wolfLeft == 0 and self.goatLeft == 0 and self.cabbageLeft == 0:
            return True
        else:
            return False

    def is_valid(self):
        #Validates positive numbers.
        if any(count < 0 for count in [self.farmerLeft, self.wolfLeft, self.goatLeft, self.cabbageLeft,
                                       self.farmerRight, self.wolfRight, self.goatRight, self.cabbageRight]):
            return False

        #Validates that the farmer is on the same side as the boat.
        if (self.boat == 'left' and self.farmerRight == 1) or (self.boat == 'right' and self.farmerLeft == 1):
            return False

        #Validates that goat is not left alone with cabbage or wolf.
        if (self.wolfLeft == self.goatLeft == 1 and self.farmerLeft == 0) or \
                (self.goatRight == self.cabbageRight == 1 and self.farmerRight == 0) or \
                (self.goatLeft == self.cabbageLeft == 1 and self.farmerLeft == 0) or \
                (self.wolfRight == self.goatRight == 1 and self.farmerRight == 0):
            return False
        return True

    def __eq__(self, other):
        return
        self.farmerLeft == other.farmerLeft and _
        self.wolfLeft == other.wolfLeft and _
        self.goatLeft == other.goatLeft and _
        self.cabbageLeft == other.cabbageLeft and _
        self.boat == other.boat and _
        self.farmerRight == other.farmerRight and _
        self.wolfRight == other.wolfRight and _
        self.goatRight == other.goatRight and _
        self.cabbageRight == other.cabbageRight

    def __hash__(self):
        return hash((self.farmerLeft, self.wolfLeft, self.goatLeft, self.cabbageLeft, self.boat, self.farmerRight,
                     self.wolfRight, self.goatRight, self.cabbageRight))


def printState(st):
    print(str(st.farmerLeft).center(15, ' ') + str(st.wolfLeft).center(17, ' ') + \
          str(st.goatLeft).center(15, ' ') + str(st.cabbageLeft).center(17, ' ') \
          + st.boat.center(7, ' ') + str(st.farmerRight).center(16, ' ') + \
          str(st.wolfRight).center(18, ' ') + \
          str(st.goatRight).center(15, ' ') + str(st.cabbageRight).center(17, ' '))


def successors(cur_state):
    children = []
    #Checks if the boat is on the left.
    if cur_state.boat == 'left':
        # Farmer & wolf move left.
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft - 1, cur_state.goatLeft, cur_state.cabbageLeft,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight + 1, cur_state.goatRight,
                          cur_state.cabbageRight)

        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # Farmer & goat move left.
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft, cur_state.goatLeft - 1, cur_state.cabbageLeft,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight, cur_state.goatRight + 1,
                          cur_state.cabbageRight)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # Farmer & cabbage move left.
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft - 1,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight, cur_state.goatRight,
                          cur_state.cabbageRight + 1)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # Farmer moves left only.
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight, cur_state.goatRight, cur_state.cabbageRight)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    else:
        # Farmer & wolf move right.
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft + 1, cur_state.goatLeft, cur_state.cabbageLeft,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight - 1, cur_state.goatRight,
                          cur_state.cabbageRight)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # Farmer & goat move right.
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft, cur_state.goatLeft + 1, cur_state.cabbageLeft,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight, cur_state.goatRight - 1,
                          cur_state.cabbageRight)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # Farmer & cabbage move right.
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft + 1,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight, cur_state.goatRight,
                          cur_state.cabbageRight - 1)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # Farmer & wolf move right.
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight, cur_state.goatRight, cur_state.cabbageRight)
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

    return children


def search():
    initial_state = State(1, 1, 1, 1, 'left', 0, 0, 0, 0)
    frontier = [initial_state]

    #Set to store explored attempts.
    explored = set()

    while frontier:
        state = frontier.pop(0)

        # Checks if goal is reached.
        if state.is_goal():
            return state

        # Adding explored states.
        explored.add(state)

        # Creates next state.
        children = successors(state)
        for child in children:
            if (child not in explored) and (child not in frontier):
                frontier.append(child)

    return None


def print_solution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print(str(state.farmerLeft).center(15, ' ') + str(state.wolfLeft).center(17, ' ') + \
              str(state.goatLeft).center(15, ' ') + str(state.cabbageLeft).center(17, ' ') \
              + state.boat.center(7, ' ') + str(state.farmerRight).center(16, ' ') + \
              str(state.wolfRight).center(18, ' ') + \
              str(state.goatRight).center(15, ' ') + str(state.cabbageRight).center(17, ' '))


def main():
    solution = search()
    print(" solution:")
    print(
        "Farmer Left | Wolf Left | Goat Left | Cabbage Left | Boat | Farmer Right | Wolf Right | Goat Right| Cabbage Right)")
    print_solution(solution)


# if called from the command line, call main()
if __name__ == "__main__":
    main()
