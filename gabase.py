from abc import ABC, abstractmethod
from individual import Individual
from population import Population
import utils

class GABase(ABC):

    def __init__(self, nodes, population_size, mutation_rate, tournament_size, elitism, salesman_num, max_distance_calculate, elite_size=None):
        self.nodes = nodes
        self.node_num = len(nodes)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elitism = elitism
        self.salesman_num = salesman_num
        self.max_distance_calculate = max_distance_calculate
        self.elite_size = elite_size
    
    @abstractmethod
    def evolve(self, population):
        pass

    @abstractmethod
    def crossover(self, individualOne, individualTwo):
        pass

    @abstractmethod
    def mutate(self, individual):
        pass

    @abstractmethod
    def select(self):
        pass
    