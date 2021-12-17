import globals
from ga import GA
from routemanager import RouteManager
from population import Population
from node import Node
import random
import matplotlib.pyplot as plt
import progressbar

pbar = progressbar.ProgressBar()
globals.init()


DATA_SET_PATH = "./data/mtsp51.txt"

nodes = globals.read_dataset(DATA_SET_PATH)

# Add Nodes
for i in range(globals.numNodes):
    RouteManager.addNode(Node(nodes[i][0], nodes[i][1]))

random.seed(globals.seedValue)
yaxis = []  # Fittest value (distance)
xaxis = []  # Generation count

pop = Population(globals.populationSize, True)
globalRoute = pop.getFittest()
print('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(globals.numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print('Global minimum distance: ' + str(globalRoute.getDistance()))
print('Final Route: ' + globalRoute.toString())

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.savefig("plot.png", dpi=400)
