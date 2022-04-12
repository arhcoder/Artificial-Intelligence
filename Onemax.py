import random
import os


'''
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      GENETIC ALGORITHM TO SOLVE THE "ONEMAX" PROBLEM      ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║  It uses the parameters:                                  ║
    ║                                                           ║
    ║      * members: Population size;                          ║
    ║      * generations: Amount of simulated generations;      ║
    ║      * couples: Max amount of couples of a generation;    ║
    ║      * mutationProbability: Between 0.0 and 1.0;          ║
    ║      * coupleProbability: Betweeen 0.0 and 0.0 and 1.0;   ║
    ║      * genes: Lenght of the genoma of each member;        ║
    ║                                                           ║
    ║  It generates a random population using the model para-   ║
    ║  meters; and then starts a simulation loop; it can do     ║
    ║  on each iteration (generation) a mutation and a couple;  ║
    ║  when there is a mutation in a son of a pair of parents,  ║
    ║  it evaluate if the mutation is better than the parent,   ║
    ║  and conserves the best gene on this case.                ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║  Last update: April 12th, 2022;                           ║
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║  @arhcoder                                                ║
    ╚═══════════════════════════════════════════════════════════╝
'''


''' MODEL PARAMETERS '''
members: int = 100
generations: int = 200
couples: int = 20
mutationProbability: float = 0.68
coupleProbability: float = 0.54
genes: int = 20




''' Random population generation '''
def generatePopulation():

    '''
        Takes the algorithm parameters and creates
        a random population based on it...

        It returns a list of lists; the list contains
        the population members...
    '''

    population = []
    member = []

    for _ in range(members):
        for _ in range(genes):
            member.append(random.randint(0, 1))
        population.append(member)
        member = []

    return population




''' Rate a member '''
def rate(member):

    '''
        Recieves a member (vector of 1's and 0's) and
        give to him a hiscore depending on his 1's
        genes (his objective performance)...
    '''

    power: int = 0
    for gene in range(genes):
        power += member[gene]
    
    return power




''' Mutation'''
def mutate(member):

    '''
        Recieves a member and mutates a random gene...
    '''

    mutationGene: int = random.randint(0, genes - 1)
    if member[mutationGene] == 0:
        member[mutationGene] = 1
    else:
        member[mutationGene] = 0




''' Couples '''
def match(firstMember, secondMember):

    '''
        Recieves a pair of members to match and makes a
        child with both genes string...

        It generates a random point on the genoma and
        put into the son the start part of the first
        member genoma (0, point), and the final part
        of the second member genoma (point + 1, 0)...
    '''

    son = []
    point: int = random.randint(0, genes)
    for i in range(0, point):
        son.append(firstMember[i])
    
    for j in range(point, genes):
        son.append(secondMember[j])

    return son




''' Evaluations '''
def best(population):

    '''
        Recieves a population and evaluate which is
        the best member and returns it...
    '''

    # To get the highest, it evaluate the first member
    # of the population as the best, then it compares
    # with the rest of the population memebers...
    bestMember = population[0]
    highestRate = rate(bestMember)

    for currentMember in range(1, members):
        currentRate: int = rate(population[currentMember])
        if currentRate > highestRate:
            bestMember = population[currentMember]
            highestRate = currentRate
        
    return bestMember

def worst(population):

    '''
        Recieves a population and evaluate which is
        the worst member and returns it...
    '''

    # To get the lower, it evaluate the first member
    # of the population as the worst, then it compares
    # with the rest of the population memebers...
    worstMember = population[0]
    lowerRate = rate(worstMember)

    for currentMember in range(1, members):
        currentRate: int = rate(population[currentMember])
        if currentRate < lowerRate:
            worstMember = population[currentMember]
            lowerRate = currentRate
        
    return worstMember




''' Main simulation '''
def simulate():

    '''
    Recreate the sumulation a prints the results of it...
    '''

    # Print the model parameters #
    print("\n\n" + 94 * "═" + "\n\n PROBLEMA \"ONE MAX\" MEDIANTE ALGORITMO GENÉTICO \n\n" + 94 * "═" + "\n")
    print(f"* Población: {members};")
    print(f"* Generaciones: {generations};")
    print(f"* Tamaño de genoma: {genes};")
    print(f"* Probabilidad de mutación: {mutationProbability * 100}%;")
    print(f"* Probabilidad de cortejo: {coupleProbability * 100}%;\n\n" + 94 * "═")
    print("\n  GENERACIÓN \t\t\tMEJOR [20]\t\t\t\t PEOR [20]\n\n" + 94 * "═" + "\n")
    
    population = generatePopulation()

    for generation in range(generations):

        for couple in range(couples):

            # Create a random courtship value, it will
            # define (with the coupleProbability value)
            # if it will be a couple...
            # If it will be a couple, it generates one
            # randomly...
            courtship: float = random.uniform(0, 1)
            if courtship < coupleProbability:

                maleIndex, femaleIndex = random.sample(range(members), 2)
                female = population[femaleIndex]
                male = population[maleIndex]

                son = match(male, female)

                # Create a random mutation value, it will
                # define (with the mutationProbability value)
                # if it will be a mutation...
                # If it will be a mutation, it generates one
                # randomly...
                mutation: float = random.uniform(0, 1)
                if mutation < mutationProbability:

                    mutate(son)
                    parentRate: int = rate(male)
                    sonRate: int = rate(son)

                    # It decides if the mutated son survive
                    # to the next generation, suppling his
                    # parent space on the population...
                    if sonRate > parentRate:
                        population[maleIndex] = son

        # Gets the best member on the generation #
        strong = best(population)
        strongRate = rate(strong)
        strongString = "".join(str(e) for e in strong)
        
        # Gets the worst member on the generation #
        weak = worst(population)
        weakRate = rate(weak)
        weakString = "".join(str(e) for e in weak)

        print(f"      {generation + 1:02d}\t\t{strongString}: [{strongRate}]\t\t{weakString}: [{weakRate}]")

        if strongRate == genes:
            print("\n" + 94 * "═" + "\n\n")
            return
    
    print("\n" + 94 * "═" + "\n\n")




''' Entry point '''
if __name__ == "__main__":
    
    # population = generatePopulation()
    # print(population)
    # print(rate(population[0]))
    # mutate(population[0])
    # match(population[0], population[1])
    # print(worst(population))
    # print(best(population))

    os.system("cls")
    simulate()