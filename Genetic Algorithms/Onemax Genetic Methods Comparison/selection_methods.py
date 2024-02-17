import random

#/ ROULETTE WHEEL SELECTION METHOD /#
def roulette_wheel(population_rates, couples_rate):

    selecteds = []
    couples = int(len(population_rates) * couples_rate / 2) * 2
    total_rate = sum(population_rates)
    indexes = list(range(len(population_rates)))
    for _ in range(couples):
        rand_point = random.uniform(0, total_rate)
        prob_sum = 0
        for i in indexes[:]:
            prob_sum += population_rates[i]
            if prob_sum >= rand_point:
                selecteds.append(i)
                indexes.remove(i)
                total_rate -= population_rates[i]
                break
    
    return selecteds


#/ RESIDUAL SELECTION METHOD /#
def residual_selection(population_rates, couples_rate):
    pass


#/ UNIVERSAL STOCHASTIC SELECTION METHOD /#
def universal_stochastic(population_rates, couples_rate):
    selecteds = []
    couples = int(len(population_rates) * couples_rate / 2) * 2
    total_rate = sum(population_rates)
    indexes = list(range(len(population_rates)))

    # Average probability:
    avg_prob = total_rate / len(population_rates)
    rand_point = random.uniform(0, avg_prob)

    for _ in range(couples):
        prob_sum = 0
        while prob_sum < rand_point:
            for i in indexes[:]:
                prob_sum += population_rates[i]
                if prob_sum >= rand_point:
                    selecteds.append(i)
                    indexes.remove(i)
                    total_rate -= population_rates[i]
                    break
        rand_point += avg_prob
    
    return selecteds


#/ TOURNAMENT SELECTION METHOD /#
def tournament_selection(population_rates, couples_rate):
    selecteds = []
    couples = int(len(population_rates) * couples_rate / 2) * 2
    indexes = list(range(len(population_rates)))

    for _ in range(couples):
        # Selects a random sample of indices for the tournament:
        tournament_indices = random.sample(indexes, int(len(indexes) * 0.5))
        
        # Gets the index of the winner (max fitness on the sample):
        winner_index = max(tournament_indices, key=lambda idx: population_rates[idx])
        selecteds.append(winner_index)
        indexes.remove(winner_index)

    return selecteds

# print(roulette_wheel([5.4, 0.2, 3.6, 8.8, 10, 9.8, 0.4, 1.4, 9.8, 7.6, 0.5, 4.3], 0.4))
# print(residual_selection([5.4, 0.2, 3.6, 8.8, 10, 9.8, 0.4, 1.4, 9.8, 7.6, 0.5, 4.3], 0.4))
# print(universal_stochastic([5.4, 0.2, 3.6, 8.8, 10, 9.8, 0.4, 1.4, 9.8, 7.6, 0.5, 4.3], 0.4))
# print(tournament_selection([5.4, 0.2, 3.6, 8.8, 10, 9.8, 0.4, 1.4, 9.8, 7.6, 0.5, 4.3], 0.4))