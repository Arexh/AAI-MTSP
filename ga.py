'''
The main helper class for Genetic Algorithm to perform
crossover, mutation on populations to evolve them
'''
from gabase import GABase
from population import Population
from individual import Individual
from ops.crossover_op import two_points_cross_baseline
from ops.mutate_op import two_salesman_mutate_baseline
import random

class GA(GABase):

    def __init__(self, nodes, population_size, mutation_rate, tournament_size, elitism, salesman_num, max_distance_calculate, elite_size):
        super(GA, self).__init__(nodes, population_size, mutation_rate, tournament_size, elitism, salesman_num, max_distance_calculate, elite_size)
        self.nodes_sorted = sorted(self.nodes)

    def evolve(self, population : Population):
        new_population = Population(self.nodes, self.salesman_num, self.population_size)

        elitism_offset = 0
        # If fittest chromosome has to be passed directly to next generation
        if self.elitism:
            new_population.individuals.append(population.find_fittest())
            elitism_offset = 1

        # Performs tournament selection followed by crossover to generate child
        for i in range(elitism_offset, self.population_size):
            parent_one = self.tournamentSelection(population)
            parent_two = self.tournamentSelection(population)
            child = self.crossover(parent_one, parent_two)
            # Adds child to next generation
            new_population.individuals.append(child)

        for i in range(elitism_offset, self.population_size):
            if random.random() < self.mutation_rate:
                self.mutate(new_population.individuals[i])

        return new_population

    # Function to implement crossover operation
    def crossover(self, parrent_one : Individual, parrent_two : Individual):
        return two_points_cross_baseline(parrent_one, parrent_two)

    # Mutation opeeration
    def mutate(self, individual : Individual):
        return two_salesman_mutate_baseline(individual)
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
        return "Baseline"