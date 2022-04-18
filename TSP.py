import random

'''

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


''''''
Roads = [
    [ 49, 28, 82, 25, 75, 24, 87, 57, 83, 11, 54, 72, 12, 55, 34,  8, 22, 59, 58, 38 ],
    [ 28, 87, 38, 27, 23, 46, 25, 88, 19,  9, 86, 39, 76, 11,  8, 78, 59, 68,  8, 35 ],
    [ 82, 38, 16, 13, 56, 51, 29, 46, 30, 63, 86, 45, 53, 59, 39, 32, 87, 81, 41, 50 ],
    [ 25, 27, 13, 18, 21, 54, 47, 20, 27, 28, 40, 54, 85, 15, 35, 59, 33, 30, 16, 34 ],
    [ 75, 23, 56, 21, 36, 42, 82, 37, 28, 60,  8, 80, 56, 14, 14, 82, 83, 10, 71, 21 ],
    [ 24, 46, 51, 54, 42, 52, 72, 65, 21, 75, 73, 27, 11, 60, 50, 29, 25, 30, 56, 30 ],
    [ 87, 25, 29, 47, 82, 72, 48, 42, 54, 57, 19, 82, 14, 84, 66, 46, 36, 27, 41, 16 ],
    [ 57, 88, 46, 20, 37, 65, 42, 57, 61, 34, 40, 13, 60, 53, 40, 43, 45, 43, 31, 56 ],
    [ 83, 19, 30, 27, 28, 21, 54, 61, 18, 85, 13, 43, 26, 83, 81, 69, 28, 66, 28, 73 ],
    [ 11,  9, 63, 28, 60, 75, 57, 34, 85, 14, 42, 87, 19, 70, 69, 83, 59, 56, 11, 46 ],
    [ 54, 86, 86, 40,  8, 73, 19, 40, 13, 42, 20, 82, 35, 65, 76, 14, 37, 63, 39, 50 ],
    [ 72, 39, 45, 54, 80, 27, 82, 13, 43, 87, 82, 24, 57, 75, 62, 19, 16, 53, 84, 66 ],
    [ 12, 76, 53, 85, 56, 11, 14, 60, 26, 19, 35, 57, 12, 43, 57, 33, 72, 35,  8,  9 ],
    [ 55, 11, 59, 15, 14, 60, 84, 53, 83, 70, 65, 75, 43, 67, 10, 79, 21, 68, 82, 29 ],
    [ 34,  8, 39, 35, 14, 50, 66, 40, 81, 69, 76, 62, 57, 10, 80, 46,  9, 27, 62, 29 ],
    [ 8,  78, 32, 59, 82, 29, 46, 43, 69, 83, 14, 19, 33, 79, 46, 36, 18, 26, 80, 23 ],
    [ 22, 59, 87, 33, 83, 25, 36, 45, 28, 59, 37, 16, 72, 21,  9, 18, 73, 24, 30, 68 ],
    [ 59, 68, 81, 30, 10, 30, 27, 43, 66, 56, 63, 53, 35, 68, 27, 26, 24, 57, 77, 71 ],
    [ 58,  8, 41, 16, 71, 56, 41, 31, 28, 11, 39, 84,  8, 82, 62, 80, 30, 77, 15, 38 ],
    [ 38, 35, 50, 34, 21, 30, 16, 56, 73, 46, 50, 66,  9, 29, 29, 23, 68, 71, 38, 80 ]
]

''''''
Tolls = [
    [ 17,  4, 31, 20, 32, 29,  7, 11, 19,  3,  8, 23, 22,  1, 10, 14, 32, 14,  0, 24 ],
    [  4,  2,  3, 33, 32, 28, 33, 11, 31, 13, 25, 18, 11, 26, 11, 33, 30, 10, 28, 28 ],
    [ 31,  3, 27,  7,  1,  2, 13, 12, 14,  4, 24,  9, 31,  7,  4, 31,  5, 27,  8, 31 ],
    [ 20, 33,  7, 33, 23, 15, 33, 13, 27, 30, 29, 12, 15, 31, 28, 21, 12, 17, 14, 21 ],
    [ 32, 32,  1, 23, 33,  4, 11,  3, 12, 24,  4, 19, 24, 22,  9, 22, 33, 11, 11, 33 ],
    [ 29, 28,  2, 15,  4, 26, 11,  4, 13, 11,  5,  8, 26, 11, 17, 11,  5,  4, 27, 26 ],
    [  7, 33, 13, 33, 11, 11,  7, 22,  5,  3,  1, 23, 14, 19, 30,  0, 18,  6, 19, 32 ],
    [ 11, 11, 12, 13,  3,  4, 22, 29, 31,  0, 15, 22, 33, 12, 12, 25, 22, 14, 27, 20 ],
    [ 19, 31, 14, 27, 12, 13,  5, 31,  3,  0,  2, 26,  7, 28, 33, 27, 33, 16,  2,  2 ],
    [  3, 13,  4, 30, 24, 11,  3,  0,  0,  4,  6, 31, 10, 17, 11, 29, 11, 18,  6,  0 ],
    [  8, 25, 24, 29,  4,  5,  1, 15,  2,  6, 11, 20,  9, 17, 25, 23, 18, 19, 17,  5 ],
    [ 23, 18,  9, 12, 19,  8, 23, 22, 26, 31, 20, 29,  6, 11, 31,  9,  5, 23,  9,  2 ],
    [ 22, 11, 31, 15, 24, 26, 14, 33,  7, 10,  9,  6,  5,  5,  4, 31,  4, 28, 11, 20 ],
    [  1, 26,  7, 31, 22, 11, 19, 12, 28, 17, 17, 11,  5,  7,  3,  4,  1, 30, 21,  0 ],
    [ 10, 11,  4, 28,  9, 17, 30, 12, 33, 11, 25, 31,  4,  3, 12, 17, 27, 18,  1, 30 ],
    [ 14, 33, 31, 21, 22, 11,  0, 25, 27, 29, 23,  9, 31,  4, 17, 19, 27, 10, 23, 11 ],
    [ 32, 30,  5, 12, 33,  5, 18, 22, 33, 11, 18,  5,  4,  1, 27, 27, 16,  0, 18, 31 ],
    [ 14, 10, 27, 17, 11,  4,  6, 14, 16, 18, 19, 23, 28, 30, 18, 10,  0,  4,  8, 20 ],
    [  0, 28,  8, 14, 11, 27, 19, 27,  2,  6, 17,  9, 11, 21,  1, 23, 18,  8, 24, 32 ],
    [ 24, 28, 31, 21, 33, 26, 32, 20,  2,  0,  5,  2, 20,  0, 30, 11, 31, 20, 32, 24 ]
]

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

    # Print the model parameters #
    print("\n\n" + 133 * "═" + "\n\n PROBLEMA \"TSP\" MEDIANTE ALGORITMO GENÉTICO \n\n" + 133 * "═" + "\n")
    print(f"* Ciudades: {cities};")
    print(f"* Población: {population};")
    print(f"* Generaciones: {generations};")
    print(f"* Probabilidad de mutación: {mutationProbability * 100}%;")
    print(f"* Probabilidad de emparejamiento: {crossoverProbability * 100}%;\n\n" + 133 * "═")
    print("\n   GENERACIÓN \t\t\t\t\t    MEJOR SOLUCIÓN\t\t\t\t\t\t  COSTO\n\n" + 133 * "═" + "\n")
    
    solutions = generateSolutions()

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