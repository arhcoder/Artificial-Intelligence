import random
from tqdm import tqdm

#/ ONEMAX GENETIC ALGORITM /#
class OnemaxGenetic:

    #* CONSTRUCTOR:
    def __init__(self, population_size: int, chromosome_size: int):

        """
            GENETIC ALGORITHM TO SOLVE ONEMAX PROBLEM

            Inputs:
                - population_size [int]: Amount of individuals on the algorithm.
                - chromosome_size [int]: Amount of genes on the chromosome.
            
            Returns:
                - OnemaxGentic object with:
                    - Attributes:
                        - best_individual [tuple]: (chromosome, fitness)
                        - population [list[tuple]]: [chromosome, ...]
                    - Methods:
                        - start_generations()
                        - restart_generations()
        """

        #? Attributes:
        self.population_size = population_size
        self.chromosome_size = chromosome_size
        self.population = list()
        self.rates = list()
        self.last_generation = 0
    

    #* METHODS:
    def generate_population(self):
        self.population = [[random.randint(0, 1) for _ in range(self.chromosome_size)] for _ in range(self.population_size)]
    

    def rate_population(self):
        self.rates = [sum(ind) for ind in self.population]
        self.best = self.population[self.rates.index(max(self.rates))]
    

    def select(self, selection_method: str, couples_rate: float = 0.4):
        selection_method = selection_method.lower()
        if couples_rate <= 0 or couples_rate > 1:
            raise ValueError("\"couples_rate\" argument must be between 0.0 and 1.0. Eg. Use 0.4 for 40%")

        from selection_methods import roulette_wheel, residual_selection, universal_stochastic, tournament_selection
        selection_methods = {
            "roulette": roulette_wheel,
            # "residual": residual_selection,
            "stochastic": universal_stochastic,
            "tournament": tournament_selection
        }
        try:
            return selection_methods.get(selection_method, None)(self.rates, couples_rate)
        except:
            print("Selected Method:", selection_method)
            raise ValueError("ERROR: Supported methods: roulette, stochastic, tournament\nNot \""+selection_method+"\"")
    

    def cross(self, couples: list, cross_method: str, points: int = 3):
        cross_method = cross_method.lower()
        if len(couples) < 3:
            raise ValueError("\"couples\" must be a list of more than 1 couple")
        if not len(couples) % 2 == 0:
            raise ValueError("\"couples\" length must be even")

        from crossover_methods import singlepoint, bipoint, multipoint, arithmetic
        crossover_methods = {
            "singlepoint": singlepoint,
            "bipoint": bipoint,
            "multipoint": multipoint,
            # "arithmethic": arithmetic
        }
        try:
            return crossover_methods.get(cross_method, None)(couples, points)
        except:
            raise ValueError("ERROR: Supported methods: singlepoint, bipoint, multipoint\nNot \""+cross_method+"\"")
    

    def mutate(self, sons: list, mutation_method: str, probability: float, univariate_probability: float = 0.2):
        mutation_method = mutation_method.lower()
        if probability < 0 and probability > 1:
            raise ValueError("\"probability\" argument must be between 0.0 and 1.0. Eg. Use 0.4 for 40%")
        if univariate_probability < 0 and univariate_probability > 1:
            raise ValueError("\"univariate_probability\" argument must be between 0.0 and 1.0. Eg. Use 0.4 for 40%")

        from mutation_methods import single_mutation, univariate_mutation
        mutation_methods = {
            "single": single_mutation,
            "univariate": univariate_mutation,
        }
        try:
            return mutation_methods.get(mutation_method, None)(sons, probability, univariate_probability)
        except:
            raise ValueError("ERROR: Supported methods: single, univariate\nNot \""+mutation_method+"\"")
    
    
    def replace(self, couples_index: list, sons: list, replacement_method: str, elitism: bool = True):
        # "couples_index" is a list of index of parents in population.
        # "sons" is a list of new individuals to replace the parents.
        if elitism:
            self.best = self.population[self.rates.index(max(self.rates))]

        if not len(couples_index) == len(sons):
            print("\nWarning! in replacement the couples_index and sons list has not the same size!")
        
        # Replacement methods:
        replacement_method = replacement_method.lower()
        if replacement_method == "parents":
            for i, couple in enumerate(couples_index):
                self.population[couple] = sons[i]
        
        elif replacement_method == "random":
            replaces = random.sample(range(len(self.population)), len(sons))
            for i, replace_index in enumerate(replaces):
                self.population[replace_index] = sons[i]
        
        elif replacement_method == "worse":
            worse_indexes = sorted(range(len(self.rates)), key=lambda i: self.rates[i])[:len(sons)]
            for i, index in enumerate(worse_indexes):
                self.population[index] = sons[i]
        
        else:
            raise ValueError("ERROR: Supported methods: parents, random, worse\nNot \""+replacement_method+"\"")
        
        # If elitism, it takes the best individual before the replacement and replaces it with the worst individual:
        if self.best:
            self.population[self.rates.index(min(self.rates))]
    
    def run(self,
                generations: int,
                stop_if_best: bool = True,
                selection_method: str = "roulette",
                couples_rate: float = 0.5,
                crossover_method: str = "singlepoint",
                points: int = 3,
                mutation_method: str = "single",
                mutation_probability: float = 0.3,
                mutation_univariate_probability: float = 0.2,
                replacement_method: str = "parents",
                elitism: bool = True,
                restart: bool = True):
        
        """
            Input:
                - "generations" [int]: Amount of generations to run.

                - "selection_method" [str]:
                    - "roulette": Roulette Wheel Method.
                    - X"residual": Residual Selection Method.
                    - "stochastic": Universal Stochastic.
                    - "tournament": Tournament Selection.

                - "couples_rate" [float]: Float betwen [0, 1] to determinate the
                percentage of the population will crossover (defalut 0.4: 40%).

                - "crossover_method" [str]:
                    - "singlepoint": Using just one point on the mixing.
                    - "bipoint": Using two points on the mixing.
                    - "multipoint": Using "n" points on mixing.
                    - X"arithmetic": Arithmetic crossover method.

                - "points" [int]: Amount of points on crossover (ONLY USABLE IF
                [selection_metdod = "multipoint"]).

                - "mutation_methods" [str]:
                    - "single": Mutate only one gene of the selected mutatation sons.
                    - "univariate": Changes each genes of selected mutation sons
                    according to "univariate_probability".

                - "mutation_probability" [float]: Between 0.0 and 1.0, defines the
                probability to mutate on the generated sons of crossover.

                - "univariate_probability" [float]: Between 0.0 and 1.0, defines
                the probability for each gene to mutate (ONLY USABLE WHEN
                [mutation_method = "univariate"]).

                - "replacement_method" [str]:
                    - "parents": Replace the sons with the parents.
                    - "random": Replace the sons with random individuals.
                    - "worse": Replace the sons with the worst individuals. 

                - "elitism" [bool]: True to hold the best individual on each
                each generation, replacing with the worst, False to don't.

                - "restart" [bool]: If True, the algorithm re-generate a new
                initial poblation and restart all the process. If False, it
                continues working with poblation generated in past runs.

            Output:
                - "best": Chromosome of the best individual obtained.
                - "rate": Rate of the individual.
                - "generation": Generation of the best individual.
        """

        print(f"\n══════════════════════════════\n       GENETIC ONEMAX\n══════════════════════════════")
        print(f" * Chromosome size: {self.chromosome_size}\n * Population size: {self.population_size}")
        print("══════════════════════════════")
        
        #* STEP 1: Generate Population:
        if restart:
            print("\nGenerating population...")
            self.generate_population()
            self.last_generation = 0
            print("Population generated!")

        #? Generational loop:
        print("\nGenerations process...")
        for generation in tqdm(range(self.last_generation, self.last_generation+generations)):
            #* STEP 2: Objetive Function Evaluation:
            self.rate_population()
            #* STEP 3: Couples Selection:
            couples = self.select(selection_method, couples_rate)
            #* STEP 4: Crossover Proess:
            couples_individuals = [self.population[i] for i in couples]
            sons = self.cross(couples_individuals, crossover_method, points)
            #* STEP 5: Mutation:
            mutations = self.mutate(sons, mutation_method, mutation_probability, mutation_univariate_probability)
            #* STEP 6: Generational Replacement:
            self.replace(couples, mutations, replacement_method, elitism=elitism)
            #* STEP 7: Revaluation:
            self.rate_population() 
            #* STEP 8: Breakpoint:
            if stop_if_best and sum(self.best) == self.chromosome_size:
                print(f"Premature solved in generation {generation}!")
                print("══════════════════════════════\n")
                return self.best, sum(self.best), generation+1
            self.last_generation += 1

        #? If not solved the problem:
        print("Generations passed!")
        print("══════════════════════════════\n")
        # print("\nBest solution founded:\n", self.best)
        return self.best, sum(self.best), generation+1