'''
The main helper class for Genetic Algorithm to perform
crossover, mutation on populations to evolve them
'''
from numpy.core.numeric import indices
from gabase import GABase
from population import Population
from individual import Individual
from ops.crossover_op import *
from ops.mutate_op import *  
import random

from utils import random_length

class NGA3(GABase):

    def __init__(self, nodes, population_size, mutation_rate, tournament_size, elitism, salesman_num, max_distance_calculate, elite_size):
        super(NGA3, self).__init__(nodes, population_size, mutation_rate, tournament_size, elitism, salesman_num, max_distance_calculate, elite_size)
        self.nodes_sorted = sorted(self.nodes)

    def evolve(self, population : Population):
        new_population = Population(self.nodes, self.salesman_num, self.population_size)

        # If fittest chromosome has to be passed directly to next generation
        for i in population.sorted_individuals()[:self.elite_size]:
            new_population.individuals.append(i)

        # Performs tournament selection followed by crossover to generate child
        for i in range(self.elite_size, self.population_size):
            parent_one = self.tournamentSelection(population)
            parent_two = self.tournamentSelection(population)
            child_one, child_two = self.crossover(parent_one, parent_two)
            # Adds child to next generation
            new_population.individuals.append(child_one)
            if len(new_population.individuals) == self.population_size:
                break
            new_population.individuals.append(child_two)
            if len(new_population.individuals) == self.population_size:
                break

        for i in range(1, self.population_size):
            if random.random() < self.mutation_rate:
                self.mutate(new_population.individuals[i])

        return new_population

    # Function to implement crossover operation
    def crossover(self, parent_one : Individual, parent_two : Individual):
        return my_cx_crossover(parent_one, parent_two)

    # Mutation opeeration
    def mutate(self, individual : Individual):
        one_slide_reverse_mutate(individual)

    # Tournament Selection: choose a random set of chromosomes and find the fittest among them
    def tournamentSelection(self, population : Population):
        tournament = Population(self.nodes, self.salesman_num, self.tournament_size)

        for i in range(self.tournament_size):
            random_int = random.randint(0, len(population.individuals) - 1)
            tournament.individuals.append(population.individuals[random_int])

        return tournament.find_fittest()

    def select(self):
        pass

    def get_name():
        return "NGA3"