import rules 
from collections import deque

def count_misplaced(state, ideal):
    """
    Counts the number of misplaced tiles in the current state compared to the ideal state.
    """
    misplaced = 0 # track misplaced tiles

    # iterate over current state and compare tile with ideal state
    for i in range(9):
        if state[i] != 0 and state[i] != ideal[i]:
            misplaced += 1

    return misplaced


def a_star_search(initial_state, ideal_state):
    """
    Conducts an A* search to find the ideal state, given an initial state.
    Returns a list of visited states, along with statistics on the search process.
    """
    node_count = 0  # count of nodes in the search tree
    max_fringe_size = 0  # maximum size of the fringe (i.e., the number of nodes that have been generated but not yet expanded)
    nodes_popped = 0  # number of nodes that have been expanded
    nodes_generated = 0  # total number of nodes that have been generated
    depth = 0  # depth of the current node in the search tree

    fringe = deque([(initial_state, depth)])  # create a deque called "fringe" containing the initial state and its depth
    visited = deque([])  # create an empty deque called "visited" to keep track of visited states
    nodes_generated += 1  # increment the count of generated nodes


    while fringe:  # while the fringe is not empty
        node_count += 1  # increment the count of nodes in the search tree
        if len(fringe) > max_fringe_size:  # if the size of the fringe is greater than the maximum size seen so far
            max_fringe_size = len(fringe)  # update the maximum size seen so far


        current_state, current_depth = fringe.popleft()  # remove the leftmost state from the fringe and assign it to "current_state" and its depth to "current_depth"
        visited.append(current_state)  # add the current state to the visited states
        nodes_popped += 1  # increment the count of popped nodes

        if current_state == ideal_state:  # if the current state is the ideal state
            return visited, node_count, nodes_generated, nodes_popped, max_fringe_size, depth  # return the visited states and search statistics

        successors = rules.get_successors(current_state)  # generate successors of the current state using the "get_successors" function from the "rules" module
        successors_copy = successors.copy()  # create a copy of the successors


        heuristic_vs = []  # create an empty list called "heuristic_vs" to store the heuristic values for each successor
        for i in range(len(successors)):  # for each successor
            if successors[i] in visited:  # if the successor has already been visited
                successors_copy.remove(successors[i])  # remove it from the copy of successors
                continue
            else:  # otherwise
                current_misplaced_tiles = count_misplaced(successors[i], ideal_state)  # calculate the number of misplaced tiles in the successor
                heuristic_vs.append(current_misplaced_tiles)  # add the heuristic value to the list
                nodes_generated += 1  # increment the count of generated nodes

        min_index = heuristic_vs.index(min(heuristic_vs))  # find the index of the successor
        fringe.append((successors_copy[min_index], current_depth + 1))
        

    return -1, -1, -1, -1, -1, -1

