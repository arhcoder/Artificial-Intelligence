
def getLinearFunction(data: dict):

    '''
        Recieves a "dict" with a linear model data;
        according to the specificactions detailed on
        "readDataSet()" from "data_reader.py" file:
        {"x": [float x values], "y": [float y values]},
        then calculates the function of a line on the
        form of f(x) = mx + c; and returns "m" and "c"
        values as tuple (m, c):

        f(x) = mx + c;
        Where:
            * "m" slope of the line.
            * "c" is "y" axis cut point.
        
        * "m" is obtained by formula:
        [ sum(x, y) - n*average(x, y) ] / [ sum(x's^2) - n*average(x's^2) ];
        Where "n" is the amount of data on x and y.

        * "c" is obtained by:
        [ average(y's) - m * average(x's) ];

        returns (m, c);
    '''

    # Gets "m" value:
    sumXY = 0
    sumXSquares = 0
    averageX = 0
    averageY = 0
    n = 0
    for i, _ in enumerate(data["x"]):
        sumXY += data["x"][i] * data["y"][i]
        sumXSquares += data["x"][i] ** 2
        averageX += data["x"][i]
        averageY += data["y"][i]
        n += 1
    averageX /= n
    averageY /= n
    # print(f"* Sum of x's * y's: {sumXY}")
    # print(f"* Sum of x's squares: {sumXSquares}")
    # print(f"* Average of x's: {averageX}")
    # print(f"* Average of y's: {averageY}")
    # print(f"* Amount of data: {n}")
    m = (sumXY - n*averageX*averageY) / (sumXSquares - n*averageX*averageX)

    # Gets "c" value:
    c = averageY - m*averageX

    # Prints the line function:
    # print(f"\n    * f(x) = {round(m, 4)}x + {round(c, 4)};")
    return (m, c)