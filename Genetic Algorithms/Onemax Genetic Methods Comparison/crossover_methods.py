import random

#/ SINGLE CROSSOVER METHOD #/
def singlepoint(couples: list, _):
    n = len(couples[0])
    if n < 2:
        raise ValueError("Chromossomes size must be > 2")
    
    # Performs the procreation:
    sons = list()
    for i in range(0, len(couples), 2):
        point = random.randint(0, n-1) + 1
        son1, son2 = list(), list()
        for j in range(0, point):
            # Couples[i] is the "father" and Couples[i+1] the "mother":
            son1.append(couples[i][j])
            son2.append(couples[i+1][j])
        for k in range(point, n):
            son2.append(couples[i][k])
            son1.append(couples[i+1][k])
        sons.append(son1)
        sons.append(son2)
    return sons


#/ BIPOINT CROSSOVER METHOD #/
def bipoint(couples: list, _):
    n = len(couples[0])
    if n < 3:
        raise ValueError("Chromossomes size must be > 3")
    
    # Performs the procreation:
    sons = list()
    for i in range(0, len(couples), 2):
        point1 = random.randint(0, n-2) + 1
        point2 = random.randint(point1, n-1) + 1
        son1, son2 = list(), list()
        
        for j in range(0, point1):
            # Couples[i] is the "father" and Couples[i+1] the "mother":
            son1.append(couples[i][j])
            son2.append(couples[i+1][j])

        for k in range(point1, point2):
            son1.append(couples[i+1][k])
            son2.append(couples[i][k])

        for l in range(point2, n):
            son1.append(couples[i][l])
            son2.append(couples[i+1][l])
        
        sons.append(son1)
        sons.append(son2)
    return sons


#/ MULTIPOINT CROSSOVER METHOD /#
def multipoint(couples: list, n: int):
    chrom_length = len(couples[0])
    if chrom_length < n+1:
        raise ValueError(f"Chromosomes size must be > {n+1}")

    # Performs the procreation:
    sons = list()
    for i in range(0, len(couples), 2):
        points = sorted(random.sample(range(1, chrom_length), n))
        points.append(chrom_length)
        son1, son2 = list(), list()
        parent_switch = True

        for j in range(len(points)):
            start_point = 0 if j == 0 else points[j-1]
            end_point = points[j]

            if parent_switch:
                # Couples[i] is the "father" and Couples[i+1] the "mother"
                son1.extend(couples[i][start_point:end_point])
                son2.extend(couples[i+1][start_point:end_point])
            else:
                son1.extend(couples[i+1][start_point:end_point])
                son2.extend(couples[i][start_point:end_point])

        parent_switch = not parent_switch
        sons.append(son1)
        sons.append(son2)
    return sons

#/ ARITHMETIC CROSSOVER METHOD /#
def arithmetic(couples: list, alpha: float = 0.5):
    if not (0 <= alpha <= 1):
        raise ValueError("Alpha must be between 0 and 1")

    chrom_length = len(couples[0])
    if chrom_length < 2:
        raise ValueError("Chromosomes size must be > 1")

    # Performs the procreation:
    sons = list()
    for i in range(0, len(couples), 2):
        son1, son2 = list(), list()

        for j in range(chrom_length):
            gene_son1 = alpha * couples[i][j] + (1 - alpha) * couples[i+1][j]
            gene_son2 = alpha * couples[i+1][j] + (1 - alpha) * couples[i][j]

            son1.append(gene_son1)
            son2.append(gene_son2)

            print("\nFather:", couples[i])
            print("Mother:", couples[i+1])
            print("Son1:", son1)
            print("Son2:", son2)


# print("\nFather:", couples[i])
# print("Mother:", couples[i+1])
# print("Points:", points[:-1])
# print("Son1:", son1)
# print("Son2:", son2)

# couples = [[1, 2, 3, 4], [5, 6, 7, 8,], [9, 10, 11, 12], [13, 14, 15, 16]]
# singlepoint(couples)

# couples = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
# bipoint(couples)

# couples = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
#     [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# ]
# multipoint(couples, 3)

# couples = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
# arithmetic(couples, 0.4)