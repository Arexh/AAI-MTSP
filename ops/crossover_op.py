from individual import Individual
import random

def two_points_cross_baseline(parrent_one : Individual, parrent_two : Individual):
    child = Individual(parrent_one.nodes, parrent_one.salesman_num)
    start_position = 0
    end_position = 0
    while (start_position >= end_position):
        start_position = random.randint(1, parrent_one.node_num - 1)
        end_position = random.randint(1, parrent_one.node_num - 1)

    for i in range(start_position + 1, end_position):
        child.node_sequence.append(parrent_one.node_sequence[i])

    left_part = []
    for node in parrent_two.node_sequence:            
        if node not in child.node_sequence:
            left_part.append(node)
        if len(left_part) == start_position:
            break
    
    child.node_sequence = left_part + child.node_sequence

    for node in parrent_two.node_sequence:
        if node not in child.node_sequence:
            child.node_sequence.append(node)
        if len(child.node_sequence) == parrent_one.node_num:
            break

    child.init_length()

    assert child.node_sequence[0] == parrent_one.nodes[0]
    assert len(child.node_sequence) == len(parrent_one.nodes)
    assert len(child.salesman_length) == parrent_one.salesman_num
    assert sorted(child.node_sequence) == sorted(parrent_one.nodes)
    return child


def one_point_crossover(parrent_one : Individual, parrent_two : Individual):
    child = Individual(parrent_one.nodes, parrent_one.salesman_num)
    split_index = random.randint(0, parrent_one.node_num - 1)

    for index in range(split_index):
        child.node_sequence.append(parrent_one.node_sequence[index])

    for index in range(parrent_one.node_num):
        if parrent_two.node_sequence[index] not in child.node_sequence:
            child.node_sequence.append(parrent_two.node_sequence[index])
        if len(child.node_sequence) == parrent_one.node_num:
            break

    child.init_length()

    assert child.node_sequence[0] == parrent_one.nodes[0]
    assert len(child.node_sequence) == len(parrent_one.nodes)
    assert len(child.salesman_length) == parrent_one.salesman_num
    assert sorted(child.node_sequence) == sorted(parrent_one.nodes)
    return child