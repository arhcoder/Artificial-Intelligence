import multiprocessing
import matplotlib.pyplot as plt
from onemaxgen import OnemaxGenetic

def run_experiment(selection_method, crossover_method, mutation_method, replacement_method, num_replications):
    # Generic data for all algorithms:
    onemax = OnemaxGenetic(
        chromosome_size=100,
        population_size=1000
    )
    # Runs for each replication:
    results = [onemax.run(
        generations=600,
        stop_if_best=True,
        elitism=False,
        selection_method=selection_method,
        crossover_method=crossover_method,
        mutation_method=mutation_method,
        replacement_method=replacement_method,

        couples_rate=0.5,
        mutation_probability=0.3,
        mutation_univariate_probability=0.3,
        points=50
    ) for _ in range(num_replications)]

    best_avg = sum(result[1] for result in results) / num_replications
    generation_avg = sum(result[2] for result in results) / num_replications

    return best_avg, generation_avg

# Replications for the experiment:
def run_replications(params):
    _, method_values, num_replications = params
    return run_experiment(*method_values, num_replications)


# Plots the runned experiments:
def plot_category_comparison(category_name, category_values, num_replications, category_index):
    # Multiprocessing:
    with multiprocessing.Pool() as pool:
        results = pool.map(run_replications, [(category_name, method_values, num_replications) for method_values in category_values])
    # Obtained results:
    avg_best_results, avg_generation_results = zip(*results)

    # Plot:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(
        [method_values[category_index] for method_values in category_values],
        avg_best_results,
        label="Fitness Máximo Promedio"
    )

    # For each bar it shows the "generation" value of the method;
    # It means that shows how many generations it takes to get the best solution:
    for i, value in enumerate(avg_generation_results):
        ax.text(i, 0.5, f"Generaciones: {value}", ha="center", va="center", color="white", fontweight="bold")
    ax.set_title(f"Mejores Fitness Obtenidos [AVG con 8 réplicas] - {category_name}")
    ax.set_ylabel("Mejor Fitness Encontrado")
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    selection_methods = [
        ("roulette", "singlepoint", "single", "parents"),
        ("stochastic", "singlepoint", "single", "parents"),
        ("tournament", "singlepoint", "single", "parents")
    ]
    crossover_methods = [
        ("roulette", "singlepoint", "single", "parents"),
        ("roulette", "bipoint", "single", "parents"),
        ("roulette", "multipoint", "single", "parents")
    ]
    mutation_methods = [
        ("roulette", "singlepoint", "single", "parents"),
        ("roulette", "singlepoint", "univariate", "parents")
    ]
    replacement_methods = [
        ("roulette", "singlepoint", "single", "parents"),
        ("roulette", "singlepoint", "single", "random"),
        ("roulette", "singlepoint", "single", "worse")
    ]

    num_replications = 8
    plot_category_comparison("Selección", selection_methods, num_replications, 0)
    plot_category_comparison("Cruzamiento", crossover_methods, num_replications, 1)
    plot_category_comparison("Mutación", mutation_methods, num_replications, 2)
    plot_category_comparison("Reemplazo", replacement_methods, num_replications, 3)