'''
Represents the chromosomes in GA's population.
The object is collection of individual routes taken by trucks.
'''
import utils
import random
import copy


class Individual:
    def __init__(self, nodes=None, salesman_num=0, instance=None):
        if instance is not None:
            self.node_num = instance.node_num
            self.salesman_num = instance.salesman_num
            self.node_sequence = copy.deepcopy(instance.node_sequence)
            self.salesman_length = copy.deepcopy(instance.salesman_length)
            self.fitness = instance.fitness
            self.nodes = instance.nodes
        else:
            self.node_num = len(nodes)
            self.salesman_num = salesman_num
            self.node_sequence = []
            self.salesman_length = []
            self.fitness = -1
            self.nodes = nodes

    def random_init(self):
        self.node_sequence = self.nodes[1:]
        random.shuffle(self.node_sequence)
        self.node_sequence = [self.nodes[0]] + self.node_sequence

        self.init_length()

        assert self.node_sequence[0] == self.nodes[0]

    def init_length(self):
        upper = self.node_num - 1
        max_bound = upper / self.salesman_num * 1.8
        min_bound = upper / self.salesman_num * 0.4
        self.salesman_length = utils.random_length_with_range(self.salesman_num, upper, min_bound, max_bound)
    
    def calculate_index(self, salesman_index, node_index):
        return sum(self.salesman_length[:salesman_index]) + node_index

    def evaluate(self):
        if self.fitness != -1:
            return 0
        else:
            distance_sum = 0
            start_index = 1
            for i in range(self.salesman_num):
                distance_sum += utils.euclidean_distance(self.node_sequence[0], self.node_sequence[start_index])
                for j in range(self.salesman_length[i] - 1):
                    start_index += 1
                    distance_sum += utils.euclidean_distance(self.node_sequence[start_index - 1], self.node_sequence[start_index])
                distance_sum += utils.euclidean_distance(self.node_sequence[start_index], self.node_sequence[0])
                start_index += 1
            self.fitness = -distance_sum
        return self.node_num + self.salesman_num * 2 - 2

    def __str__(self) -> str:
        return "\nNode sequence: " + str(self.node_sequence) + "\n" + "Each individual: " + str(self.salesman_length)

# i = Individual([], 10)
# 1531.2219430620278
# i.node_sequence = [[37,52],[61,33],[21,10],[17,33],[46,10],[42,57],[62,63],[20,26],[10,17],[59,15],[30,15],[25,55],[37,69],[51,21],[32,22],[8,52],[30,40],[45,35],[31,32],[48,28],[56,37],[58,27],[52,64],[49,49],[42,41],[5,6],[27,23],[39,10],[30,48],[27,68],[12,42],[21,47],[38,46],[31,62],[63,69],[52,41],[7,38],[43,67],[40,30],[32,39],[52,33],[58,48],[62,42],[57,58],[36,16],[13,13],[17,63],[5,64],[5,25],[25,32],[16,57],]
# i.salesman_length = [6, 5, 5, 5, 8, 4, 4, 6, 4, 3]
# i.evaluate()
# print(i.fitness)
# [6, 5, 5, 5, 8, 4, 4, 6, 4, 3]

# i.node_sequence = [[37,52],[58,27],[61,33],[46,10],[58,48],[25,32],[5,25],[17,33],[52,64],[43,67],[57,58],[56,37],[45,35],[52,41],[32,39],[52,33],[20,26],[37,69],[31,62],[27,23],[42,57],[38,46],[30,15],[59,15],[36,16],[13,13],[39,10],[51,21],[48,28],[21,47],[31,32],[10,17],[32,22],[42,41],[25,55],[21,10],[62,63],[63,69],[7,38],[16,57],[17,63],[30,48],[8,52],[30,40],[49,49],[62,42],[40,30],[5,64],[27,68],[5,6],[12,42]]
# 1485.1595929055936
# i.salesman_length = [4, 3, 4, 6, 4, 8, 3, 5, 7, 6]
# i.evaluate()
# print(i.fitness)