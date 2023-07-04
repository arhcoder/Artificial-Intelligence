import csv

def readDataSetFrom(CSVFilePath: str):

    '''
        Recieves the path of a CSV file and reads
        from it the data of points to fins the
        Linear Regression.

        The file has to be on the next form:
        ╔                   ╗
            titlex,titley
            12,80.82
            14,88.24
            16,90
            10,68.4
            8.2,58.2
        ╚                   ╝
        Only two columns, where the first column
        has the x's values (independent variable),
        and the second one the y's values (dependent
        variable); separated by commas.
        * THE FIRST ROW HAS TO CONTAIN THE TITLES!

        It returns a data structure (map) that
        contains x values with key name "x", same to
        y values; and the columns titles on "titles".
        NOTE: For x and y values, it converts it into
        real numbers.
        For example:
        For file:
        ╔                       ╗
            Study hours,Note
            1,4.2
            2,5.0
            3,6.2
            4,8.8
            5,10
        ╚                       ╝
        It returns:
        {
            "titles": "Study hours", "Note",
            "x": [1, 2, 3, 4, 5],
            "y": [4.2, 5.0, 6.2, 8.8, 10]
        }
    '''

    with open(CSVFilePath, "r") as file:
        try:
            x: list = []
            y: list = []
            titles: list = []
            title = False
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                if not title:
                    titles.append(str(row[0]))
                    titles.append(str(row[1]))
                    title = True
                else:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
            return {"titles": titles, "x": x, "y": y}
                
        except Exception:
            return print(f"Error to read {CSVFilePath};\n{Exception}")