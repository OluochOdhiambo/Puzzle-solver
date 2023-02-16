import rules
from collections import deque

def breadth_first_search(initial_state, ideal_state):
    node_count = 0
    max_fringe_size = 0
    nodes_expanded = 0
    nodes_generated = 0
    depth = 0

    fringe = deque([(initial_state, depth)])
    visited = []

    states_and_successors = {}

    visited.append(tuple(initial_state))
    nodes_generated += 1
    
    while fringe:
        node_count += 1
        if len(fringe) > max_fringe_size:
            max_fringe_size = len(fringe)

        current_state, current_depth = fringe.popleft()

        if current_state == ideal_state:
            parents_list = deque([])
            searching = True
            search_term = ""
            iterrations = 1

            while searching:
                if search_term == "":
                    parents_list.append(ideal_state)
                    search_term = ideal_state

                if iterrations < current_depth and search_term != "":
                    for parent, children in states_and_successors.items():
                        if search_term in children:
                            search_term = parent.strip('][').split(', ')
                            search_term = [int(x) for x in search_term]
                            parents_list.append(search_term)
                            break
                        else: 
                            continue
                else: 
                    searching = False

                iterrations += 1
            
            parents_list.append(initial_state)

            return node_count, nodes_expanded, nodes_generated, max_fringe_size, current_depth, parents_list

        nodes_expanded += 1
        successors = rules.get_successors(current_state)

        # Combine current state and successors
        if states_and_successors.get(str(current_state)) is None:
            states_and_successors[str(current_state)] = successors


        # Testing code
        for successor in successors:
            if tuple(successor) in visited or successor == initial_state:
                continue
            else:
                fringe.append((successor, current_depth + 1))
                visited.append(tuple(successor))
                nodes_generated += 1
                

    return -1, -1, -1, -1, -1, -1
