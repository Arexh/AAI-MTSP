from ga import GA
from routemanager import RouteManager
from population import Population
import random
import matplotlib.pyplot as plt
import progressbar
import numpy as np
import utils
from nga2 import NGA2
from ga import GA

numGenerations = 100
# size of population
populationSize = 100
mutationRate = 1
tournamentSize = 10
elitism = True
# number of trucks
numTrucks = 5
seedValue = 1
elite_size = 1

DATA_SET_PATH = "./data/pr226.txt"

widgets = ['Progress: ', progressbar.Percentage(), ' ', progressbar.Bar('#'), ' ', progressbar.Timer(),
           ' ', progressbar.ETA()]
pbar = progressbar.ProgressBar(widgets=widgets)

nodes = utils.read_dataset(DATA_SET_PATH)

# random.seed(seedValue)
yaxis = []  # Fittest value (distance)
xaxis = []  # Generation count

pop = Population(nodes, numTrucks, populationSize)
pop.random_init()
globalRoute = pop.find_fittest()
print('Initial minimum distance: ' + str(-globalRoute.fitness))
ga = NGA2(nodes=nodes,
          population_size=populationSize,
          mutation_rate=mutationRate,
          tournament_size=tournamentSize,
          elitism=elitism,
          salesman_num=numTrucks,
          elite_size=elite_size,
          max_distance_calculate=20000)

# Start evolving
for i in pbar(range(numGenerations)):
    pop = ga.evolve(pop)
    localRoute = pop.find_fittest()
    print(localRoute.fitness)
    if globalRoute.fitness < localRoute.fitness:
        globalRoute = localRoute
    yaxis.append(-localRoute.fitness)
    xaxis.append(i)

print('Global minimum distance: ' + str(-globalRoute.fitness))
print('Final Route:', globalRoute)

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.savefig("plot.png", dpi=400)

assert len(np.unique(globalRoute.node_sequence, axis=0)) == len(nodes)
assert sorted(globalRoute.node_sequence) == sorted(nodes)
