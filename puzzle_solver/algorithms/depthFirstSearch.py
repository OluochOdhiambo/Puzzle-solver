import rules

def is_goal(config, goal_config):
    return config == goal_config

def dfs(init_st, goal_st, config, visited, moves, nodes_generated, nodes_popped, depth):
    nodes_generated += 1
    path_exists = True

    if is_goal(config, goal_st):
        return moves, nodes_generated, nodes_popped, path_exists, depth
    
    successors = rules.get_successors(config)
    
    for neighbor in successors:
        if neighbor not in visited:
            if neighbor in moves:
                break
            result = dfs(init_st, goal_st, neighbor, visited + [config], moves + [neighbor], nodes_generated, nodes_popped + 1, depth + 1)
            if result is not None:
                return result

        nodes_popped += 1
    
    path_exists = False

    return None, nodes_generated, nodes_popped, path_exists, depth


def depth_first_search(init_st, goal_st):

    initial_successors = rules.get_successors(init_st)

    path_exists = False
    successor_index = 0
    moves = None
    successful_child = None

    while path_exists == False and successor_index < len(initial_successors):
        moves, nodes_generated, nodes_popped, path_exists, current_depth = dfs(init_st, goal_st, initial_successors[successor_index], [], [initial_successors[successor_index]], 0, 0, 1)
        successor_index += 1

    if moves is not None:
        successful_child = initial_successors[successor_index - 1]
        parents = moves[::-1]
        return parents, successful_child, nodes_generated, nodes_popped, path_exists, current_depth
    else:
        return -1, -1, nodes_generated, nodes_popped, path_exists, current_depth
