import math


def Initialize():
    list = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    return list


def calculate_cost(state):
    countingInvaesion = 0
    length = len(state)
    for i in range(length-1):
        for j in range(i+1, length):
            if state[i] > state[j]:
                countingInvaesion += 1
    return countingInvaesion


def generate_neighbors(current_state):
    neighbors = []
    length = len(current_state)
    for i in range(length-1):
        new_list = current_state.copy()
        for j in range(i, length-1):
            new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
            neighbors.append(new_list.copy())
    return neighbors


def State_generation(current_state):
    while True:
        current_state_cost = calculate_cost(current_state)
        print("Current State:", current_state, "->", current_state_cost)
        min_next_cost = math.inf
        min_next_state = None
        neighbors = generate_neighbors(current_state)
        length = len(neighbors)
        for i in range(length):
            next_state = neighbors[i]
            next_state_cost = calculate_cost(next_state)
            if next_state_cost < current_state_cost:
                min_next_cost = next_state_cost
                min_next_state = next_state
                break
        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print("Final State:", current_state, "->", current_state_cost)
            break


State_generation(Initialize())
