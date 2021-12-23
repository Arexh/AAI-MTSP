from individual import Individual
import random
import utils


def two_points_cross_baseline(parent_one: Individual, parent_two: Individual):
    child = Individual(parent_one.nodes, parent_one.salesman_num)
    start_position = 0
    end_position = 0
    while (start_position >= end_position):
        start_position = random.randint(1, parent_one.node_num - 1)
        end_position = random.randint(1, parent_one.node_num - 1)

    for i in range(start_position + 1, end_position):
        child.node_sequence.append(parent_one.node_sequence[i])

    left_part = []
    for node in parent_two.node_sequence:
        if node not in child.node_sequence:
            left_part.append(node)
        if len(left_part) == start_position:
            break

    child.node_sequence = left_part + child.node_sequence

    for node in parent_two.node_sequence:
        if node not in child.node_sequence:
            child.node_sequence.append(node)
        if len(child.node_sequence) == parent_one.node_num:
            break

    child.init_length()

    assert child.node_sequence[0] == parent_one.nodes[0]
    assert len(child.node_sequence) == len(parent_one.nodes)
    assert len(child.salesman_length) == parent_one.salesman_num
    assert sorted(child.node_sequence) == sorted(parent_one.nodes)
    return child


def one_point_crossover(parent_one: Individual, parent_two: Individual):
    child = Individual(parent_one.nodes, parent_one.salesman_num)
    split_index = random.randint(0, parent_one.node_num - 1)

    for index in range(split_index):
        child.node_sequence.append(parent_one.node_sequence[index])

    for index in range(parent_one.node_num):
        if parent_two.node_sequence[index] not in child.node_sequence:
            child.node_sequence.append(parent_two.node_sequence[index])
        if len(child.node_sequence) == parent_one.node_num:
            break

    child.init_length()

    assert child.node_sequence[0] == parent_one.nodes[0]
    assert len(child.node_sequence) == len(parent_one.nodes)
    assert len(child.salesman_length) == parent_one.salesman_num
    assert sorted(child.node_sequence) == sorted(parent_one.nodes)
    return child

def my_cx_crossover_list(parent_one: list, parent_two: list) -> list:
    length = len(parent_one)
    assert len(parent_one) == len(parent_two)
    child_one = [None] * length
    child_two = [None] * length
    value_index = 0

    def get_next(parent_one, parent_two, value_index):
        return parent_one.index(parent_two[value_index])
    for index in range(length):
        if parent_two[value_index] in child_one:
            if sorted(child_one[:index]) == sorted(child_one[:index]):
                for index_two in range(length):
                    if parent_two[index_two] not in child_one:
                        value_index = index_two
                        break
            else:
                while parent_two[value_index] in child_one:
                    value_index = get_next(parent_one, parent_two, value_index)
        # assign child one
        child_one[index] = parent_two[value_index]
        # find next value index for child two
        value_index = get_next(parent_one, parent_two, value_index)
        # assign child two
        child_two[index] = parent_one[value_index]
        # update value index
        value_index = get_next(parent_one, parent_two, value_index)

    return child_one, child_two

def my_cx_crossover(parent_one: Individual, parent_two: Individual):
    child_one = Individual(instance=parent_one)
    child_two = Individual(instance=parent_two)

    sequence_one, sequence_two \
         = my_cx_crossover_list(parent_one.node_sequence, parent_two.node_sequence)

    child_one.node_sequence = sequence_one
    child_two.node_sequence = sequence_two

    child_one.fitness = -1
    child_two.fitness = -1

    assert sum(child_one.salesman_length) == parent_one.node_num - 1
    assert sorted(child_one.node_sequence) == sorted(parent_one.nodes)
    assert sum(child_two.salesman_length) == parent_one.node_num - 1
    assert sorted(child_two.node_sequence) == sorted(parent_one.nodes)
    return child_one, child_two

if __name__ == "__main__":
    pass