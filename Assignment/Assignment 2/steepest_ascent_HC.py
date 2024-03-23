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
    for i in range(len(current_state)):
        for j in range(i+1, len(current_state)):
            new_state = current_state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)
    return neighbors


def State_generation(current_state):
    while True:
        current_state_cost = calculate_cost(current_state)
        print("Current State:", current_state, "------", current_state_cost)

        min_next_cost = math.inf
        min_next_state = None

        for neighbor in generate_neighbors(current_state):
            next_state = neighbor
            next_state_cost = calculate_cost(next_state)
            if next_state_cost < min_next_cost:
                min_next_cost = next_state_cost
                min_next_state = next_state
        if min_next_cost < current_state_cost:
            print("Better neighbor found")
            current_state = min_next_state
        else:
            print("Final State:", current_state, "------", current_state_cost)
            break


State_generation(Initialize())
