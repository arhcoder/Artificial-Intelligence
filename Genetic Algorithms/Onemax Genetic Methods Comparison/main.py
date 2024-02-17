from onemaxgen import OnemaxGenetic

onemax = OnemaxGenetic(chromosome_size=100, population_size=1000)
best, rate, generation = onemax.run(
    generations=600,
    stop_if_best=True,
    selection_method="roulette",
    couples_rate=0.5,
    crossover_method="singlepoint",
    points=1,
    mutation_method="single",
    mutation_probability=0.3,
    mutation_univariate_probability=0.3,
    replacement_method="parents",
    elitism=True
)
print(f"BEST:\n * Individual: {best}\n * Rate: {(rate/100)*100:.2f}%\n * Generation: {generation+1}\n")