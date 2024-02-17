from onemaxgen import OnemaxGenetic

chromo_size = 100
onemax = OnemaxGenetic(chromosome_size=chromo_size, population_size=1000)
best, rate, generation = onemax.run(
    generations=600,
    stop_if_best=True,
    selection_method="roulette",
    couples_rate=0.5,
    crossover_method="singlepoint",
    mutation_method="single",
    mutation_probability=0.1,
    mutation_univariate_probability=0.3,
    replacement_method="random",
    elitism=True,
    restart=True
)
print(f"BEST:\n * Individual: {best}\n * Rate: {(rate/chromo_size)*100:.2f}%\n * Generation: {generation}\n")