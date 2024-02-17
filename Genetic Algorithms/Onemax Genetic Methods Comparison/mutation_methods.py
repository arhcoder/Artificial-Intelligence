import random

#/ SINGLE MUTATION METHOD /#
def single_mutation(sons: list, probability: float, _):
    for son in sons:
        # The son mutates:
        if random.random() <= probability:
            point = random.randint(0, len(son)-1)
            son[point] = 1 if son[point] == 0 else 0
    return sons


#/ UNIVARIATE MUTATION METHOD /#
def univariate_mutation(sons: list, probability: float, univariate_probability):
    for son in sons:
        # The son mutates:
        if random.random() <= probability:
            for i in range(len(son)):
                if random.random() <= univariate_probability:
                    son[i] = 1 if son[i] == 0 else 0
    return sons


# sons = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]
# single_mutation(sons, 0.4)
# univariate_mutation(sons, 0.4, 0.3)