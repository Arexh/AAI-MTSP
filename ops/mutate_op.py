from individual import Individual
import random

def two_salesman_mutate_baseline(individual : Individual):
    index_one = 0
    index_two = 0
    while index_one == index_two:
        index_one = random.randint(0, individual.salesman_num - 1)
        index_two = random.randint(0, individual.salesman_num - 1)

    if index_one > index_two:
        index_one, index_two = index_two, index_one

    # generate replacement range for 1
    salesman_one_start = 0
    salesman_one_end = 0
    while salesman_one_start > salesman_one_end or salesman_one_start == 0:
        salesman_one_start = random.randint(0 if index_one != 0 else 1, individual.salesman_length[index_one])
        salesman_one_end = random.randint(0, individual.salesman_length[index_one])
    
    # generate replacement range for 2
    salesman_two_start = 0
    salesman_two_end = 0
    while salesman_two_start > salesman_two_end or salesman_two_start == 0:
        salesman_two_start = random.randint(0, individual.salesman_length[index_two])
        salesman_two_end = random.randint(0, individual.salesman_length[index_two])

    swap_one = []  # values from 1
    swap_two = []  # values from 2

    
    for i in range(salesman_two_start, salesman_two_end + 1):
        swap_two.append(individual.node_sequence.pop(individual.calculate_index(index_two, salesman_two_start)))
    # pop all the values to be replaced
    for i in range(salesman_one_start, salesman_one_end + 1):
        swap_one.append(individual.node_sequence.pop(individual.calculate_index(index_one, salesman_one_start)))

    length_diff = len(swap_one) - len(swap_two)

    # add to new location by pushing
    first_insert = individual.calculate_index(index_one, salesman_one_start)
    second_insert = individual.calculate_index(index_two, salesman_two_start) - length_diff
    individual.node_sequence[first_insert:first_insert] = swap_two
    individual.node_sequence[second_insert:second_insert] = swap_one

    individual.salesman_length[index_one] -= length_diff
    individual.salesman_length[index_two] += length_diff
    individual.fitness = -1

    assert sum(individual.salesman_length) == individual.node_num - 1
    assert sorted(individual.node_sequence) == sorted(individual.nodes)


def one_slide_reverse_mutate(individual : Individual):
    index_one, index_two = random.sample(range(1, individual.node_num), 2)
    slide = individual.node_sequence[index_one:index_two]
    slide.reverse()
    individual.node_sequence[index_one:index_two] = slide
    
    individual.fitness = -1

    assert sum(individual.salesman_length) == individual.node_num - 1
    assert sorted(individual.node_sequence) == sorted(individual.nodes)

def two_point_swap_mutate(individual : Individual):
    index_one, index_two = random.sample(range(1, individual.node_num), 2)
    individual.node_sequence[index_one], individual.node_sequence[index_two] = \
        individual.node_sequence[index_two], individual.node_sequence[index_one]
    
    individual.fitness = -1

    assert sum(individual.salesman_length) == individual.node_num - 1
    assert sorted(individual.node_sequence) == sorted(individual.nodes)