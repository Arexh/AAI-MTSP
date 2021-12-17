import random

'''
Contains all global variables specific to simulation
'''


def init():
    global xMax, yMax, seedValue, numNodes,\
        numGenerations, populationSize, mutationRate, tournamentSize,\
        elitism, numTrucks
    # Defines range for coordinates when nodes are randomly scattered
    xMax = 1000
    yMax = 1000
    seedValue = 1
    numNodes = 200
    numGenerations = 70
    # size of population
    populationSize = 100
    mutationRate = 0.02
    tournamentSize = 10
    elitism = True
    # number of trucks
    numTrucks = 10


def random_range(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

# Randomly distribute number of nodes to subroutes
# Maximum and minimum values are maintained to reach optimal result


def route_lengths():
    upper = (numNodes + numTrucks - 1)
    fa = upper/numTrucks*1.6  # max route length
    fb = upper/numTrucks*0.6  # min route length
    a = random_range(numTrucks, upper)
    while 1:
        if all(i < fa and i > fb for i in a):
            break
        else:
            a = random_range(numTrucks, upper)
    return a


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
