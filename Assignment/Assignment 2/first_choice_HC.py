import math


def Initialize():
    initial_list = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    return initial_list


def calculate_cost(state):
    inversion_count = 0
    length = len(state)
    for i in range(length-1):
        for j in range(i+1, length):
            if state[i] > state[j]:
                inversion_count += 1
    return inversion_count


def generate_neighbors(current_state):
    neighbors = []
    length = len(current_state)
    for i in range(length):
        new_list = current_state.copy()
        if i < length - 1:
            new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
            neighbors.append(new_list)
    return neighbors


def State_generation(current_state):
    while True:
        current_state_cost = calculate_cost(current_state)
        print("Current State:", current_state, "------", current_state_cost)
        min_next_cost = math.inf
        min_next_state = None
        neighbors = generate_neighbors(current_state)
        for next_state in neighbors:
            next_state_cost = calculate_cost(next_state)
            if next_state_cost < current_state_cost:
                print("Better neighbor found")
                current_state = next_state
                current_state_cost = next_state_cost
                break
        else:
            print("Final State:", current_state, "------", current_state_cost)
            break


State_generation(Initialize())
