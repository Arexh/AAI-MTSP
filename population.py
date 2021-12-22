'''
Collection of routes (chrmosomes)
'''
from individual import Individual

class Population:

    def __init__(self, nodes, salesman_num, population_size):
        self.population_size = population_size
        self.individuals = []
        self.nodes = nodes
        self.salesman_num = salesman_num

    def random_init(self):
        for i in range(self.population_size):
            individual = Individual(self.nodes, self.salesman_num)
            individual.random_init()
            self.individuals.append(individual)

    def evaluate(self):
        calculation_times = 0
        for individual in self.individuals:
            if individual.fitness == -1:
                calculation_times += individual.evaluate()
        return calculation_times

    def find_fittest(self):
        self.evaluate()
        return max(self.individuals, key=lambda x : x.fitness)

    def sorted_individuals(self):
        self.evaluate()
        return sorted(self.individuals, key=lambda x : x.fitness, reverse=True)
