import argparse
import os
from collections import deque
from algorithms import breadthFirstSearch as bfs
from algorithms import depthFirstSearch as dfs
from algorithms import aStarSearch as astar

parser = argparse.ArgumentParser(description="solves the 8 puzzle problem")

parser.add_argument('--heuristic_search', metavar='heuristic_search', type=str, help='choose search algorithm', default="bfs", choices=["bfs", "a*", "dfs"])
parser.add_argument('--initial_state', metavar='initial_state', type=str, help='set puzzle initial state as an array i.e [1,2,3,4,5,0,7,8,6]')
parser.add_argument('--goal_state', metavar='goal_state', type=str, help='set puzzle goal state as an array i.e [1,2,3,4,5,6,7,8,0]')
parser.add_argument('--dump', metavar='dump', type=bool, help="dump data to txt", default=False, choices=[True, False])

args = parser.parse_args()

# Args
heuristic_search = args.heuristic_search
dump = args.dump
initial_state = args.initial_state.strip('[]').split(",")
goal_state = args.goal_state.strip('[]''').split(', ')
initial_state = [int(i) for i in list(args.initial_state.strip('[]').split(","))]
goal_state = [int(i) for i in list(args.goal_state.strip('[]').split(','))]

# Vars
node_count = None
nodes_expanded = None
nodes_generated = None
max_fringe_size = None 
current_depth = None 
states_and_successors = None

# print in grid format
def print_in_format(matrix):
    for i in range(9):
        if i%3 == 0 and i > 0:
            print("")
        print(str(matrix[i]) + " ", end = "")

def is_solvable(state):
        inversion_count = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                    inversion_count += 1

        return inversion_count % 2 == 0

def get_play_sequence(parents): 
    directions = deque([])

    def motion_tracker(current_state, previous_state):
        current_zero_index = current_state.index(0)
        previous_zero_index = previous_state.index(0)
        direction = current_zero_index - previous_zero_index

        if direction == 1:
            #  0 moves right number moves left
            return [previous_state[current_zero_index], "left"]
        elif direction == -1:
            #  0 moves left number moves right
            return [previous_state[current_zero_index], "right"]
        elif direction == -3:
            #  0 moves down number moves up
            return [previous_state[current_zero_index], "down"]
        elif direction == 3:
            #  0 moves up number moves down
            return [previous_state[current_zero_index], "up"]

    for i in range(len(parents) - 1):
        current_state_index = i
        previous_state_index = i + 1
        direction = motion_tracker(parents[current_state_index], parents[previous_state_index])
        directions.appendleft(direction)   

    return directions

def play(sequence):
    while sequence:
        move = sequence.pop()
        print("Move " + str(move[0]) + " " + move[1])

def write_to_file(init_st, goal_st, algorithm, stats):
    lines = ["Nodes generated", "Nodes popped",  "Current depth"]
    if os.path.exists('tracedump.txt'):
        with open('tracedump.txt', 'a') as f:
            f.write("Dump for " + algorithm + " algorithm")
            f.write('\n')
            f.write("Initial state " + str(init_st))
            f.write('\n')
            f.write("Final state " + str(goal_st))
            f.write('\n')
            for i in range(len(lines)):
                f.write(lines[i] + " : " + str(stats[i]))
                f.write('\n')

    else:
        with open('tracedump.txt', 'w') as f:
            f.write("Dump for " + algorithm + " algorithm")
            f.write('\n')
            f.write("Initial state " + str(init_st))
            f.write('\n')
            f.write("Final state " + str(goal_st))
            f.write('\n')
            for i in range(len(lines)):
                f.write(lines[i] + " : " + str(stats[i]))
                f.write('\n')

    

def main(init_st, goal_st, algorithm):
    if is_solvable(init_st) != True:
        print("Puzzle is not solvable.")
        return

    if algorithm == "bfs":
        node_count, nodes_popped, nodes_generated, max_fringe_size, current_depth, parents_list = bfs.breadth_first_search(init_st, goal_st)
        if dump:
            write_to_file(init_st, goal_st, "bfs", [nodes_generated, nodes_popped, current_depth])
        directions = get_play_sequence(parents_list)
        play(directions)

    elif algorithm == "a*":
        visited, node_count, nodes_generated, nodes_popped, max_fringe_size, current_depth = astar.a_star_search(init_st, goal_st)
        if dump:
            write_to_file(init_st, goal_st, "bfs", [nodes_generated, nodes_popped, current_depth])
        directions = get_play_sequence(visited)
        play(directions)

    elif algorithm == "dfs":
        moves, successful_child, nodes_generated, nodes_popped, path_exists, current_depth = dfs.depth_first_search(init_st, goal_st)
        if dump:
            write_to_file(init_st, goal_st, "bfs", [nodes_generated, nodes_popped, current_depth])
        if moves != -1:
            directions = get_play_sequence(moves)
            play(directions)
        else:
            print("Couldn't find solution. Try different algorithm")


if __name__ == "__main__":
    main(initial_state, goal_state, heuristic_search)