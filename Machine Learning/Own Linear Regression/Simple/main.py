from data_reader import readDataSetFrom
from get_line import getLinearFunction
from graphic import graphLinearModel

if __name__ == "__main__":

    #? Models to analize:
    models = [

        ("STUDENTS GRADES ACCORDING TO HIS STUDY HOURS",
        "data/students-notes.csv"),

        ("SALARY ACCORDING TO EXPERIENCE YEARS",
        "data/salary-data.csv"),

        ("USA VIOLENT CRIMES (ALL)",
        "data/crimes-usa-all.csv"),

        ("CALIFORNIA VIOLENT CRIMES (MURDER)",
        "data/crimes-california-murder.csv"),

        ("NEW YORK VIOLENT CRIMES (RAPE)",
        "data/crimes-ny-rape.csv")
    ]

    #* Analize each model:
    for source in models:
        print("\n", 60*"-")
        print(f"\n 🌐 Analizing from {source[1]}")
        data = readDataSetFrom(source[1])
        line = getLinearFunction(data)

        print(" 📈 Opening plot...")
        graphLinearModel(data, line, source[0], source[1])
        print(" ✅ Analysis done!")
    print("\n", 60*"-", "\n")