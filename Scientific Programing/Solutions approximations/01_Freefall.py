from math import e
from os import system, times
from bokeh.plotting import figure, output_file, show


'''
    ╔════════════════════════════════════════════════════════╗
    ║  ANÁLISIS COMPUTACIONAL DE UN PROBLEMA DE CAÍDA LIBRE  ║
    ║  MEDIANTE MÉTODO EXACTO Y MÉTODO APROXIMADO.           ║
    ╚════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════╗
    ║  Escrito por Alejandro Ramos @arhcoder.                ║
    ╚════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════╗
    ║  Fecha: Febrero 4, 2022.                               ║
    ╚════════════════════════════════════════════════════════╝
'''


''' PARÁMETROS DEL MODELO '''

bodyWeight: float = 60.0
gravity: float = 9.80
resistence: float = 12.5
timeIncrement: float = 0.5
timeLimit: float = 20.0

''' LISTAS PARA GRÁFICAS '''
times = []
exactVelocities = []
approximatedVelocities = []


def exactVelocityOn(time: float):
    
    '''
        Recibe la variable time [float], y retorna un valor
        de velocidad en mts/s, con la función exacta:

        v(t) = [mg / c][1 - e^((-c/m)t)];

        donde:
        m: Masa del cuerpo (kg);
        g: Constante de gravitación (mts por s);
        c: Constante de resistencia del viento;
        t: Tiempo en segundos a evaluar (s);
    '''

    return ((bodyWeight * gravity) / resistence) * (1 - e ** ((-resistence / bodyWeight) * time))

''' Variables para la simulación de método aproximado '''
deltaTime: float = 0.0
approximatedVelocitie: float = 0.0
def approximatedVelocityOn(time: float, previousTime: float):

    '''
        Recibe la variable time [float], y retorna un valor
        de velocidad en mts/s, con la función aproximada:

        v(ti+1) = [g - (c * v(ti) / m)][(ti+1) - ti][v(ti)];

        donde:
        m: Masa del cuerpo (kg);
        g: Constante de gravitación (mts por s);
        c: Constante de resistencia del viento;
        ti: Tiempo actual a evaluar (s);
        ti - 1: Tiempo de la iteración anterior (s);
    '''

    velocity = gravity - ((resistence * previousTime) / bodyWeight)
    if time != 0: deltaTime = time - timeIncrement
    else: deltaTime = 0.0
    velocity = velocity * (time - deltaTime)

    return velocity + previousTime


if __name__ == '__main__':

    '''
        Solicita datos del modelo como la masa del cuerpo,
        cociente de resistencia del aire e incremento de
        tiempo y crea un loop que evalua imprime en una
        tabla los valores de la velocidad en caída libre,
        para un objeto con los datos definidos para el
        modelo; usando un método exacto, y uno aproximado,
        graficando la relación de velocidad de ambos métodos,
        con respecto a la velocidad, y llegando hasta t = 20s;
    '''

    # Limpia consola #
    system("cls")

    # Pide datos #
    print("\n║ MODELO DE CAÍDA LIBRE ║\n\nVelocidad de un paracaidísta al caer con:\n")
    bodyWeight = float(input("* Masa del paracaidísta (kilogramos): "))
    resistence = float(input("* Constante de resistencia del aire (decimal): "))
    timeIncrement = float(input("* Incremento en el tiempo (segundos): "))

    # Imprime los datos de una tabla #
    print("\n ╔" + "═" * 74 + "╗")
    print(" ║" + " " * 74 + "║")
    print(" ║\tTiempo \t\t Velocidad Exacta\t Velocidad Aproximada" + " " * 6 + " ║")
    print(" ║\t(Seg)\t\t    (Mts/seg)\t\t      (Mts/seg)\t\t    ║")
    print(" ║" + " " * 74 + "║")
    print(" ╠" + "═" * 74 + "╣")
    print(" ║" + " " * 74 + "║")

    # Inicia el ciclo de iteraciones #
    time = 0.0
    while time <= timeLimit:

        exactVelocitie = exactVelocityOn(time)
        exactVelocities.append(exactVelocitie)

        approximatedVelocitie = approximatedVelocityOn(time, approximatedVelocitie)
        approximatedVelocities.append(approximatedVelocitie)

        times.append(time)

        print(f" ║\t {time:.1f}\t\t   {exactVelocitie:.9f}\t\t      {approximatedVelocitie:.9f}\t    ║")
        time += timeIncrement
    
    # Imprime el final de la tabla #
    print(" ║" + " " * 74 + "║")
    print(" ╚" + "═" * 74 + "╝\n")


    # Crea el gráfico #
    print("Generando gráfica...")
    FreefallGraphic = figure(title = "COMPARACIÓN DE MÉTODO EXACTO Y APROXIMADO EN CAÍDA LIBRE", x_axis_label = "Tiempo transcurrido (Seg)", y_axis_label = "Velocidad calculada (Mts/seg)")
    output_file("01_Freefall-Graphic.html")
    FreefallGraphic.line(times, exactVelocities, legend_label = "Método Exacto", line_color = "blue", line_width = 2)
    FreefallGraphic.line(times, approximatedVelocities, legend_label = "Método Aproximado", line_color = "red", line_width = 2)
    show(FreefallGraphic)
    print("Gráfica generada")