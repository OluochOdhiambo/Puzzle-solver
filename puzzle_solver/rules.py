def get_successors(state):
        zero_index = state.index(0)
        row = zero_index // 3
        col = zero_index % 3

        successors = []

        if row > 0:
            new_state = state.copy()
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            successors.append(new_state)

        if row < 2:
            new_state = state.copy()
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            successors.append(new_state)

        if col > 0:
            new_state = state.copy()
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            successors.append(new_state)

        if col < 2:
            new_state = state.copy()
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            successors.append(new_state)

        return successors