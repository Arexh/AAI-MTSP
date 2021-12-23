from population import Population
import matplotlib.pyplot as plt
import progressbar
import numpy as np
import random
import os
import json
import scipy.stats
import utils
from nga2 import NGA2
from ga import GA as baseline
import time

POPULATION_SIZE = 100
MUTATION_RATE = 1
TOURNAMENT_SIZE = 10
ELITISM = True
SALESMAN_NUM = 5
SEED_VALUE = 1
ELITE_SIZE = 1
TIMES = 30

start_time = time.time()

random.seed(SEED_VALUE)

ALGORITHMS = [baseline, NGA2]
DATASETS = ["mtsp51", "mtsp100", "mtsp150", "pr76", "pr152", "pr226"]
# DATASETS = ["mtsp51"]
RESULT_PATH = "./results/"

result_log = {}

if not os.path.exists(RESULT_PATH):
    os.makedirs(RESULT_PATH)

for dataset in DATASETS:
    index = 0
    baseline_every_gen = []
    ours_every_gen = []
    baseline_best = []
    ours_best = []
    current_dataset_log = {}
    for algorithm in ALGORITHMS:
        current_algorithm_log = {
            "BestDistance": [],
            "GenerationDistance": [],
            "AverageDistance": []
        }
        for t in range(TIMES):
            widgets = ['Data: ', dataset, ', Alg: ', algorithm.get_name(), ', Progress: ', progressbar.Percentage(), ', ', progressbar.Bar('#'), ', ', progressbar.Timer(), ', ', progressbar.ETA(), ', ', progressbar.DynamicMessage("current_best_result")]
            nodes = utils.read_dataset("./data/" + dataset + ".txt")
            numGenerations = int(20000 * len(nodes) / utils.one_calculate_times(SALESMAN_NUM, len(nodes)) / (POPULATION_SIZE - 1))
            pop = Population(nodes, SALESMAN_NUM, POPULATION_SIZE)
            pop.random_init()
            globalRoute = pop.find_fittest()

            ga = algorithm(nodes=nodes,
                            population_size=POPULATION_SIZE,
                            mutation_rate=MUTATION_RATE,
                            tournament_size=TOURNAMENT_SIZE,
                            elitism=ELITISM,
                            salesman_num=SALESMAN_NUM,
                            elite_size=ELITE_SIZE,
                            max_distance_calculate=20000)

            pbar = progressbar.ProgressBar(widgets=widgets)
            fitnesses = []
            # Start evolving
            for i in pbar(range(numGenerations)):
                pop = ga.evolve(pop)
                localRoute = pop.find_fittest()
                pbar.dynamic_messages.current_best_result = -localRoute.fitness
                if globalRoute.fitness < localRoute.fitness:
                    globalRoute = localRoute
                fitnesses.append(-localRoute.fitness)

            if index == 0:
                baseline_every_gen.append(fitnesses)
                baseline_best.append(-globalRoute.fitness)
            else:
                ours_every_gen.append(fitnesses)
                ours_best.append(-globalRoute.fitness)

            assert len(np.unique(globalRoute.node_sequence, axis=0)) == len(nodes)
            assert sorted(globalRoute.node_sequence) == sorted(nodes)
            current_algorithm_log['AverageDistance'].append(sum(fitnesses) / len(fitnesses))
            current_algorithm_log['GenerationDistance'].append(fitnesses)
            current_algorithm_log['BestDistance'].append(-globalRoute.fitness)
        
        if index == 0:
            current_dataset_log["Baseline"] = current_algorithm_log
        else:
            current_dataset_log["Ours"] = current_algorithm_log
        index += 1
        
    # plot every generation's fitness
    fig, ax = plt.subplots()

    baseline_every_gen = np.array(baseline_every_gen)
    ours_every_gen = np.array(ours_every_gen)

    plt.fill_between(range(baseline_every_gen.shape[1]), np.max(baseline_every_gen, axis=0), np.min(baseline_every_gen, axis=0), interpolate=True, color='#a5d2ff')
    plt.plot(np.mean(baseline_every_gen, axis=0), color="dodgerblue", label="Baseline")
    plt.fill_between(range(ours_every_gen.shape[1]), np.max(ours_every_gen, axis=0), np.min(ours_every_gen, axis=0), interpolate=True, color='#abd0bb')
    plt.plot(np.mean(ours_every_gen, axis=0), color="seagreen", label="Ours")

    ranksum_test = scipy.stats.ranksums(baseline_best, ours_best)

    current_dataset_log['Statistic'] = ranksum_test[0]
    current_dataset_log['PValue'] = ranksum_test[1]

    ax.legend(loc='upper right', frameon=False)
    plt.title(dataset + " dataset (" + str(TIMES) + " runs)")
    plt.xlabel("Generation")
    plt.ylabel("Distance")
    plt.savefig(RESULT_PATH + dataset + "(all).eps", format='eps')
    
    # plot every best fitness
    fig, ax = plt.subplots()
    plt.plot(baseline_best, color="dodgerblue", label="Baseline")
    plt.plot(ours_best, color="seagreen", label="Ours")
    plt.plot([sum(baseline_best) / len(baseline_best)] * len(baseline_best), label='Baseline Average', linestyle='--')
    plt.plot([sum(ours_best) / len(ours_best)] * len(ours_best), label='Ours Average', linestyle='--')
    ax.legend(frameon=False)
    plt.title(dataset + " dataset (" + str(TIMES) + " runs)")
    plt.xlabel("Run")
    plt.ylabel("Best Distance")
    plt.savefig(RESULT_PATH + dataset + "(best).eps", format='eps')

    result_log[dataset] = current_dataset_log

with open(RESULT_PATH + 'result_log.json', 'w') as f:
    json.dump(result_log, f, indent=4)

print("Finish time:", time.time() - start_time)