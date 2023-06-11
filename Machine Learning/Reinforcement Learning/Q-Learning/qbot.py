import random

#/ ---------------------------------------------- VARIABLES ---------------------------------------------- /#


info = '''

    ═════════════════════════════════════════════════════════════════

    QBOT - Q-LEARNING PARA EL APRENDIZAJE POR REFUERZO

    ═════════════════════════════════════════════════════════════════

    Esta es la implementación de un agente (llamado "QBot"),
    que simula a un robot tratando de llegar de un punto "A"
    a un punto "B", en una cuadrícula 2D, con el camino que
    más beneifico le traiga. Con las siguientes reglas:

    1. El terreno es cuadriculado.

    2. Se tiene un punto de inicio.

    3. Se tiene un punto de final.

    4. Cada cuadro puede contener:

        - Nada [-];
        - Obstáculo [x];
        - Recompenza [+];

    5. Al dar un paso sobre un recuadro vacío, se pierde
    [1 puntos] en el puntaje de la ruta tomada por el robot.

    6. No se puede dar un paso sobre un obstáculo.

    7. Al dar un paso sobre una recompensa, se gana [1 puntos].

    8. Al llegar a la salida se ganan [100 puntos].

    El objetivo de esta implementación, es que mediante un
    método de Machine Learning ("Q-Learning" que es una
    técnica de Aprendizaje por Refuerzo) se pueda encontrar
    EL MEJOR CAMINO DEL INICIO AL FIN, el cual consiste en;
    EL CAMINO QUE DEJE UN MAYOR PUNTAJE (ES DECIR, QUE MENOS
    PASOS DÉ, PERO QUE DEJE LA MAYOR CANTIDAD DE RECOMPENSAS).

    ═════════════════════════════════════════════════════════════════
'''
print("\n", info)


#* VARIABLES DE ENTRENAMIENTO:
learning_rate = 0.2
discount_factor = 0.8
exploration_rate = 0.4
iterations = 2000


#/ Tablero:
#? "S": Inicio.
#? "E": Final.
#? "X": Obstáculo.
#? "O": Premio.
#? " ": Vacío.
board = [
    ["S",  " ",  " ",  " ",  " ",  " ",  "X",  " ",  " ",  " "],
    [" ",  " ",  " ",  " ",  "O",  " ",  " ",  " ",  " ",  " "],
    [" ",  " ",  "X",  " ",  " ",  " ",  " ",  " ",  "X",  " "],
    [" ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " "],
    [" ",  " ",  "O",  " ",  " ",  "X",  " ",  " ",  "O",  " "],
    ["X",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " "],
    [" ",  " ",  " ",  "X",  "O",  " ",  "X",  " ",  " ",  " "],
    [" ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " "],
    [" ",  "X",  " ",  " ",  " ",  " ",  "X",  " ",  " ",  " "],
    [" ",  " ",  " ",  "X",  " ",  "O",  " ",  " ",  " ",  "E"]
]


#/ Acciones:
#? ---------- 0 -------- 1 -------- 2 ------- 3 ----- ;
actions = ["arriba", "derecha", "abajo", "izquierda"]


#/ Construye el tablero pero con los datos de recompenza:
#? Este tablero contendrá los números enteros que representan los datos del tablero:
rewards = []
for row in board:
    reward_row = []
    for box in row:
        if box == "S":
            reward_row.append(int(0))
        elif box == " ":
            reward_row.append(int(-1))
        elif box == "O":
            reward_row.append(int(1))
        elif box == "X":
            reward_row.append(int(-100))
        elif box == "E":
            reward_row.append(int(100))
        else:
            reward_row.append(str("x"))
    rewards.append(reward_row)


#/ ---------------------------------------------- IMPRESIONES ---------------------------------------------- /#

def print_board(board):
    print(f"╔"+"═"*52+"╗")
    for i, row in enumerate(board):
        print("║ ", end="")
        for box in row:
            if box == " ":
                print("     ", end="")
            elif box == "S":
                print("🤖   ", end="")
            elif box == "S":
                print("□     ", end="")
            elif box == "E":
                print("   → ", end="")
            elif box == "O":
                print("💎   ", end="")
            elif box == "X":
                print("██   ", end="")

            elif box == "u":
                print(" ↑   ", end="")
            
            elif box == "r":
                print(" →   ", end="")

            elif box == "d":
                print(" ↓   ", end="")
            
            elif box == "l":
                print(" ←   ", end="")
        
        if i < len(board) - 1:
            print(" ║")
        else:
            print("  ")

    print(f"╚"+"═"*52)


print("TABLERO INICIAL")
print_board(board)
input("\nPresione una tecla para iniciar entrenamiento...")

#/ ---------------------------------------------- FUNCIONES ---------------------------------------------- /#

# Entrenando el agente utilizando Q-Learning:
def train_agent(rewards, learning_rate, discount_factor, exploration_rate, iterations):
    '''
        Esta función entrena al agente utilizando el algoritmo de Q-Learning.
        Toma como entrada el tablero de recompensas, la tasa de aprendizaje, el factor de descuento,
        la tasa de exploración y la cantidad de iteraciones para el entrenamiento.

        Retorna la tabla Q que representa los valores de acción para cada estado.
    '''

    # Inicializar la tabla Q:
    Q = {}

    # Inicia las iteraciones para el entrenamiento:
    for iteration in range(iterations):

        # Posición inial por defecto:
        position = (0, 0)
        episode_reward = 0

        # Realiza movimientos hasta llegar al estado objetivo:
        while position != (len(rewards)-1, len(rewards[0])-1):

            # Elige una acción aleatoria o la acción miximizada en la tabla Q:
            if random.random() < exploration_rate:
                action = random.randint(0, 3)
            else:
                # Si la posición no está en la tabla Q, se inicializa por defecto:
                if position not in Q:
                    Q[position] = [0, 0, 0, 0]
                action = Q[position].index(max(Q[position]))
            
            # Realiza la acción y obtener la nueva posición y la recompensa:
            new_position, reward = perform_action(position, action)

            # Si la nueva posición no está en la tabla Q, se inicializa por defecto:
            if new_position not in Q:
                Q[new_position] = [0, 0, 0, 0]
            
            # Obtiene el valor máximo de acción para la nueva posición:
            max_q_value = max(Q[new_position])

            # Actualizar el valor Q para la posición y acción actual utilizando la ecuación de Q-Learning:
            Q[position][action] = (1 - learning_rate) * Q[position][action] + learning_rate * (reward + discount_factor * max_q_value)

            # Actualizar la recompensa acumulada en el episodio:
            episode_reward += reward

            # Actualizar la posición actual del robot:
            position = new_position
        
        # Imprime el desempeño al terminar la iteración:
        print(f"Iteración {iteration+1}; Recompensa total: {episode_reward};")
    
    return Q


# Obteniendo las acciones posibles desde una posición dada:
def get_possible_actions(position):
    '''
        Esta función devuelve las acciones posibles desde una posición dada en el tablero.
        Recibe como entrada la posición actual del agente.
        Retorna una lista de las acciones posibles (representadas por valores enteros).
    '''
    x, y = position
    possible_actions = []

    # Comprueba si es posible moverse hacia:
    # Arriba:
    if x > 0:
        possible_actions.append(0)
    # Abajo:
    if x < len(rewards)-1:
        possible_actions.append(2)
    # Izquierda:
    if y > 0:
        possible_actions.append(3)
    # Derecha:
    if y < len(rewards[0])-1:
        possible_actions.append(1)
    
    return possible_actions


# Eligiendo una acción utilizando una política epsilon-greedy:
def choose_action(Q, position, possible_actions, exploration_rate):
    '''
        Esta función elige una acción utilizando una política epsilon-greedy.
        Recibe como entrada la tabla Q, la posición actual del agente, las acciones posibles
        desde esa posición y la tasa de exploración.
        Retorna la acción elegida según la política epsilon-greedy.
    '''

    # Exploración: Elige una acción aleatoria de las posibles:
    if random.random() < exploration_rate:
        return random.choice(possible_actions)
    # Explotación: Elige la acción con el mayor valor Q:
    else:
        x, y = position
        max_q_value = max([Q[x][y] for y in possible_actions])
        max_q_actions = [action for action in possible_actions if Q[x][y] == max_q_value]
        return random.choice(max_q_actions)


# Realizando una acción en una posición dada:
def perform_action(position, action):
    '''
        Esta función realiza una acción desde una posición dada en el tablero y devuelve la nueva posición y la recompensa.
        Recibe como entrada la posición actual del agente y la acción a realizar.
        Retorna la nueva posición y la recompensa obtenida al realizar la acción.
    '''

    # Determinar la nueva posición según la acción elegida:
    x, y = position
    # Arriba:
    if action == 0:
        new_x = x - 1
        new_y = y
    # Derecha:
    elif action == 1:
        new_x = x
        new_y = y + 1
    # Abajo:
    elif action == 2:
        new_x = x + 1
        new_y = y
    # Izquierda:
    elif action == 3:
        new_x = x
        new_y = y - 1
    
    # Verifica si las nuevas coordenadas están fuera de los límites del tablero:
    if new_x < 0 or new_x >= len(rewards) or new_y < 0 or new_y >= len(rewards[0]):

        # Devuelve la posición actual y una recompensa de -100 por salirse:
        return position, -100
    
    # Si no se salió del tablero, retorna la nueva posición y recompenza:
    return (new_x, new_y), rewards[new_x][new_y]


# Actualizando la tabla Q utilizando la ecuación de Q-Learning:
def update_q_table(Q, current_position, action, new_position, reward, learning_rate, discount_factor):

    '''
        Esta función actualiza la tabla Q utilizando la ecuación de Q-Learning.

        Recibe como entrada la tabla Q, la posición actual del agente, la acción realizada,
        la nueva posición resultante, la recompensa obtenida, la tasa de aprendizaje y el factor de descuento.

        No retorna ningún valor, pero actualiza la tabla Q con los nuevos valores calculados.

        La ecuación utilizada es:
            Q(s, a) = (1 - learning_rate) * Q(s, a) + learning_rate * (reward + discount_factor * max Q(s', a'))
    '''

    # Valores de referencia en el movimiento:
    x, y = current_position
    new_x, new_y = new_position

    # Obtiene el máximo valor Q de la nueva posición:
    max_q_value = max(Q[new_x][new_y]) if isinstance(Q[new_x][new_y], list) else 0

    # Actualiza el valor Q para la acción realizada en la posición actual:
    Q[x][y][action] = (1 - learning_rate) * Q[x][y][action] + learning_rate * (reward + discount_factor * max_q_value)


# Encontrando la recompensa total de un camino:
def get_total_score(Q):
    '''
        Esta función calcula el puntaje total de la ruta encontrada por el robot.

        Recibe como entrada la tabla Q que representa las acciones y sus valores asociados.

        Retorna el puntaje total de la ruta encontrada por el robot.

        La función realiza un recorrido desde la posición inicial hasta la posición final,
        siguiendo las acciones con el mayor valor Q en cada posición, y acumulando el puntaje obtenido en cada paso.
    '''

    # Posición inicial:
    position = (0, 0)
    total_score = 0

    # Simula el paso a paso para obtener la recompensa:
    while position != (len(rewards)-1, len(rewards[0])-1):

        # Obtiene la acción con el mayor valor Q:
        action = Q[position].index(max(Q[position]))

        # Realiza la acción y obtiene la nueva posición y recompensa:
        position, reward = perform_action(position, action)

        # Suma el valor del paso:
        total_score += reward
    
    return total_score


#/ ---------------------------------------------- IMPLEMENTACIÓN ---------------------------------------------- /#
print("\nENTRENAMIENTO")
#? Se crea una instancia de Tabla Q para entrenar al robotsito:
try:
    Q = train_agent(rewards, learning_rate, discount_factor, exploration_rate, iterations)

    #? Inicia el camino utilizando el entrenamiento:
    optimal_path = []
    position = (0, 0)

    #? Para cada paso obtiene el tipo de acción (arriba, derecha, abajo, izquieda):
    while position != (len(rewards)-1, len(rewards[0])-1):
        action = Q[position].index(max(Q[position]))
        optimal_path.append(actions[action])
        position, _ = perform_action(position, action)

    #! Imprime la mejor ruta obtenida:
    print("\nCAMINO ÓPTIMO")
    print(" → ".join(action.capitalize() for action in optimal_path)+";")


    #! Crea e imprime el tablero con la ruta:
    def create_board_with_directions(board, optimal_path):
        new_board = [[box for box in row] for row in board]

        directions = {
            "arriba": "u",
            "derecha": "r",
            "abajo": "d",
            "izquierda": "l"
        }

        position = (0, 0)
        for action in optimal_path:
            x, y = position
            if action == "arriba":
                x -= 1
            elif action == "derecha":
                y += 1
            elif action == "abajo":
                x += 1
            elif action == "izquierda":
                y -= 1
            
            if board[x][y] == "O":
                new_board[x][y] = "O"
            else:
                new_board[x][y] = directions[action]
            
            position = (x, y)

        return new_board

    new_board = create_board_with_directions(board, optimal_path)
    print_board(new_board)
    input("\nQBot encontró el camino correcto 😎\n")

except Exception as error:
    print("\nUN ERROR OCURRIÓ DURANTE EL ENTRENAMIENTO, PASA MUY POCAS VECES!")
    print("Por favor ejecuta de nuevo todo este proyecto, esperándo no encontrar el error de nuevo :c")
    print("Confía en mí, es muy poco común, no debería afectarte muy seguido si pruebas de nuevo el programa :3\n\n")
    # print(error)