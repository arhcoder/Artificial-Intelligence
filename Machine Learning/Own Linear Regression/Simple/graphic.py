import matplotlib.pyplot as plt
import numpy as np

def graphLinearModel(data: dict, line: tuple, title: str, source: str):
    
    '''
        Recieves a "dict" with a linear model data;
        according to the specificactions detailed on
        "readDataSet()" from "data_reader.py" file:
        {"x": [float x values], "y": [float y values]}.

        Recieves a tuple of line function values: (m, c);
        "m" is the slope, "c" is the y axis cut point.

        It also recieves the source to put in the graph.

        Use matplotlib to graph the points on the model
        (on data's x and y) and the line according to
        f(x) = mx + c;
    '''

    # Generates the graphic:
    figure, ax = plt.subplots(figsize = (10, 10))
    plt.suptitle(title)
    plt.title(f"From \"{source}\"\n")
    plt.xlabel(data["titles"][0])
    plt.ylabel(data["titles"][1])

    # Graphs the points:
    ax.scatter(data["x"], data["y"], color="#DE0B0B", zorder=3)

    # Graphs the line:
    axes = plt.gca()
    xseq = np.array(axes.get_xlim())
    ax.plot(xseq, line[1] + line[0] * xseq, label=f"f(x) = {round(line[0], 2):,}x + {round(line[1], 2):,};", color="#1844C2", lw=2.4, zorder=4);

    # Shows the graphic:
    plt.legend(loc="upper center")
    plt.grid(zorder=0)
    plt.show()