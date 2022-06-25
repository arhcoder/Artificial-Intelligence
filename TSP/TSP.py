import random
import csv

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx



'''
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      GENETIC ALGORITHM TO SOLVE THE "TSP" PROBLEM         ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║  It uses the parameters:                                  ║
    ║                                                           ║
    ║      * members: Population size;                          ║
    ║      * generations: Amount of simulated generations;      ║
    ║      * mutationProbability: Between 0.0 and 1.0;          ║
    ║      * coupleProbability: Betweeen 0.0 and 0.0 and 1.0;   ║
    ║       * cities: Amount of cities of the problem;          ║
    ║                                                           ║
    ║   This algorithm recieves (plus the model parameters),    ║
    ║   two network graphs as adjacency matrices that           ║
    ║   represents:                                             ║
    ║                                                           ║
    ║       * Distances between each city.                      ║
    ║       * Tolls to pay in each road of the cities.          ║
    ║                                                           ║
    ║   Using these and two more parameters (processed like     ║
    ║   multiobjective optimization functions):                 ║
    ║                                                           ║
    ║       * roadsDistancesPorcentualImportance;               ║
    ║       * tollsCostPorcentualImportance;                    ║
    ║                                                           ║
    ║   Both with 100% relation; generates a random population  ║
    ║   of solutions (set of numbers between [0 cities - 1] of  ║
    ║   size "cities + 1", that no repeats numbers, expecting   ║
    ║   the first (it is repeated at the end of the set):       ║
    ║   [1, 4, 8, 5, 3, 7, 6, 0, 2, 1];) and; in each           ║
    ║   generation, mutate and cross some of them to improve    ║
    ║   them; extracting the best solution on each generation,  ║
    ║   and the best on whole the population history.           ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║  Last update: April 18th, 2022;                           ║
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║  @arhcoder                                                ║
    ╚═══════════════════════════════════════════════════════════╝
'''

''' MODEL PARAMETERS '''
population: int = 1000
generations: int = 1000
mutationProbability: float = 1.0
crossoverProbability: float = 1.0

# With the 100% relation #
roadsDistancesPorcentualImportance: float = 0.68
tollsCostPorcentualImportance: float = 0.32

''' PROBLEM VARIABLES '''
cities = 20


''' ADJACENCY MATRIX OF ROADS DISTANCES BETWEEN CITIES '''

# Takes the matrix from TSP/Roads.csv #
Roads = []
with open("TSP/Roads.csv", "r", newline = "") as file:
    myreader = csv.reader(file, delimiter = ",")
    for rows in myreader:
        Roads.append(rows)

# It convert to int matrix in case that it takes as string matrix #
for n, i in enumerate(Roads):
    for k, j in enumerate(i):
        Roads[n][k] = int(j)


''' ADJACENCY MATRIX OF TOLLS COSTS IN EACH ROAD '''

# Taken from TSP/Tolls.csv #
Tolls = []
with open("TSP/Tolls.csv", "r", newline = "") as file:
    myreader = csv.reader(file, delimiter = ",")
    for rows in myreader:
        Tolls.append(rows)

# It convert to int matrix in case that it takes as string matrix #
for n, i in enumerate(Tolls):
    for k, j in enumerate(i):
        Tolls[n][k] = int(j)


# df = pd.DataFrame(Roads)
# df.to_csv("MyRoads.csv")




''' BEST SOLUTION ON WHOLE THE SIMULATION '''
king = []




''' Random solutions (population) generation '''
def generateSolutions():

    ''''
        Generates a random population of solutions.
        It takes the model variables to do it.

        A solution is a set of numbers between [0
        cities - 1] of size "(cities + 1)", that
        no repeats numbers, expecting the first
        (it is repeated at the end of the set)...
        
        For example:

            With nine cities:
            [1, 4, 8, 5, 3, 7, 6, 0, 2, 1];

        The functions returns a set of
        ("population") solutions...
    '''

    solutions = []
    solution = []

    for _ in range(population):
        solution[:] = random.sample(range(cities), cities)
        solution.append(solution[0])
        solutions.append(solution)
        solution = []

    return solutions




''' Gets the costs of a solution tour '''
def tour(solution):

    '''
        It recieves a solution (list of no-
        repeated int numbers) and; using the
        model varibales and the distances &
        tolls graphs, evaluate the solution
        cost, and returns a list of two
        elements: distance and tolls cost...
    '''

    # Takes the tour on the distances graph #
    distance = 0;
    for index in range(cities):
        distance += Roads[solution[index]][solution[index + 1]]
    
    # Takes the tour on the tolls graph #
    tolls = 0;
    for index in range(cities):
        tolls += Tolls[solution[index]][solution[index + 1]]
    
    return [distance, tolls]




''' Multiobjective optimization rating '''
def rate(solution):

    '''
        It recieves a solution, and using
        the "rate()" function, it gets the
        distance cost and the tolls cost
        of the solution, then calculates
        the final cost of the solution
        (float) based on the ponderation
        variables of the costs, like an
        objective function of a
        multiobjective optimization
        problem, and returns it...
    '''

    costs = tour(solution)

    return (costs[0] * roadsDistancesPorcentualImportance) + (costs[1] * tollsCostPorcentualImportance)




''' Evaluation of the best solution '''
def best(solutions):

    '''
        It recieves a population of solutions
        and evalueates which is the best.
        It returns the solution...
    '''

    # To get the highest, it evaluate the first member
    # of the population as the best, then it compares
    # with the rest of the population memebers...
    bestSolution = solutions[0]
    highestRate = rate(bestSolution)

    for currentSolution in range(1, population):
        currentRate: int = rate(solutions[currentSolution])
        if currentRate < highestRate:
            bestSolution = solutions[currentSolution]
            highestRate = currentRate
        
    return bestSolution




''' Mutation '''
def mutate(solution):

    '''
        It recieves a solution, and swap
        two random values of it...
    '''

    points = []
    points[:] = random.sample(range(0, cities), 2)


    # "Mutation" saves the solution without the last value.
    mutation = solution[:cities]
    mutation[points[0]], mutation[points[1]] = mutation[points[1]], mutation[points[0]]
    mutation.append(mutation[0])

    solution = mutation




''' Crossover '''
def crossover(first, second):

    '''
        It recieves a couple of solutions
        and cross they, and returns the
        generated solution...
    '''

    crossPoint = random.randint(1, cities - 1)
    cross = second[:cities]
    for i in range(crossPoint):
        cross.remove(first[i])
    cross.extend(first[:crossPoint])
    cross.append(cross[0])

    return cross




''' Simulation point '''
def simulation():

    '''
        Recreate the sumulation a prints the results of it...
    '''


    # It exports the local matrix to csv files... #
    # with open("TSP/Roads.csv", "w", newline = "") as file:
    #     mywriter = csv.writer(file, delimiter = ",")
    #     mywriter.writerows(Roads)
    
    # with open("TSP/Tolls.csv", "w", newline = "") as file:
    #     mywriter = csv.writer(file, delimiter = ",")
    #     mywriter.writerows(Tolls)


    # Print the model parameters #
    print("\n\n" + 133 * "═" + "\n\n PROBLEMA \"TSP\" MEDIANTE ALGORITMO GENÉTICO \n\n" + 133 * "═" + "\n")
    print(f"* Ciudades: {cities};")
    print(f"* Población: {population};")
    print(f"* Generaciones: {generations};")
    print(f"* Probabilidad de mutación: {mutationProbability * 100}%;")
    print(f"* Probabilidad de emparejamiento: {crossoverProbability * 100}%;\n\n" + 133 * "═")
    print("\n   GENERACIÓN \t\t\t\t\t    MEJOR SOLUCIÓN\t\t\t\t\t\t  COSTO\n\n" + 133 * "═" + "\n")
    
    solutions = generateSolutions()

    global king
    king = solutions[0]

    for generation in range(generations):

        for _ in range(generations // 2):

            # If it will be a cross #
            if random.uniform(0, 1) <= crossoverProbability:

                firstSolutionIndex, secondSolutionIndex = random.sample(range(population), 2)
                firstSolution = solutions[firstSolutionIndex]
                secondSolution = solutions[secondSolutionIndex]
                cross = crossover(firstSolution, secondSolution)

                # If it will be a mutation #
                if random.uniform(0, 1) <= mutationProbability:

                    mutate(cross)
                    parentCost: int = rate(firstSolution)
                    crossCost: int = rate(cross)

                    # It decides if the mutated cross survive
                    # to the next generation, suppling his
                    # parent space on the solutions...
                    if crossCost <= parentCost:
                        solutions[firstSolutionIndex] = cross

        # Gets the best member on the generation #
        strong = best(solutions)
        strongRate = rate(strong)

        # Update the best member on whole the history #
        if rate(strong) <= rate(king):
            king = strong

        print(f"      {generation + 1:02d}\t\t{strong}\t\t{strongRate:04f}")
    
    print("\n" + 133 * "═" + "\n")
    print(f"SOLUCIÓN: {king}: {rate(king)};")
    print("\n" + 133 * "═" + "\n\n")




''' Graphics generation '''
def generateGraph():

    '''
        Generates a graphic based on the roads graph
        drawing also the best path founded...
    '''

    # Draws the matrix #
    NumpyMatrix = np.array(Roads)
    Graph = nx.from_numpy_matrix(NumpyMatrix)
    Position = nx.spring_layout(Graph)
    nx.draw_networkx(Graph, pos = Position, node_color = "#50A8FA", node_size = 400, edge_color = "#08080866")
    # nx.draw_networkx_nodes(Graph, pos = Position, node_color = "#8B4DFF")
    # nx.draw_networkx_edges(Graph, pos = Position, alpha = 0.4)

    # Converts the king solution into a tuple of nodes #
    global king
    path = []
    for node in range(len(king) - 1):
        path.append((king[node], king[node + 1]))

    # Draws the path #
    Path = nx.DiGraph(Graph)
    nx.draw_networkx_edges(Path, pos = Position, edgelist = path, width = 1.4, edge_color = "red")

    # Generates the graphic #
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.title("TSP: Camino más corto encontrado")
    plt.savefig("TSP/Graph.png")
    plt.show()




''' Entry point '''
if __name__ == "__main__":

    # print(generateSolutions())
    # graph = [
    #     [0, 5, 10, 30],
    #     [5, 0, 12, 4],
    #     [10, 12, 0, 20],
    #     [30, 4, 20, 0]
    # ]

    # rate(graph, [0, 1, 3, 2, 0])
    # print(tour([2, 1, 4, 5, 3, 0, 2]))
    # print(rate([2, 1, 4, 5, 3, 0, 2]))
    # print(mutate([2, 1, 4, 5, 3, 0, 2]))
    # print(crossover([2, 1, 4, 5, 3, 0, 2], [4, 0, 3, 1, 5, 2, 4]))

    # solutions = generateSolutions()
    # for solution in solutions:
    #     costs = rate(solution)
    #    print(f"{solution}: {costs[0]:02f};\t{costs[1]:02f};\t{costs[2]:02f};\t")

    simulation()
    generateGraph()