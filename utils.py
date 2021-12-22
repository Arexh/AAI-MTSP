import random
import numpy as np

'''
Contains all global variables specific to simulation
'''

def random_length(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def random_length_with_range(n, total, lower, upper):
    temp_result = random_length(n, total)
    while 1:
        if all(i > lower and i < upper for i in temp_result):
            break
        else:
            temp_result = random_length(n, total)
    return temp_result

def euclidean_distance(node_one, node_two):
    assert len(node_one) == len(node_two)
    return np.linalg.norm(np.array(node_one) - np.array(node_two))

def is_not_blank(s):
    return bool(s and not s.isspace())


def read_dataset(p):
    global numNodes
    with open(p) as f:
        node = []
        numNodes = int(f.readline())
        for line in f.read().splitlines():
            if is_not_blank(line):
                temp_list = line.split(' ')
                node.append([int(temp_list[1]), int(temp_list[2])])
        return node
