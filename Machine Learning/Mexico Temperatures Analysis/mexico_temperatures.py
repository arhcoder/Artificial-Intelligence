import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# It gets a CSV with world temperatures changes on earth:
temperatures = pd.read_csv("./Data/Temperatures/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")

# Describes the info on the Data Frame:
print("\n", temperatures.info())
print("\n", temperatures.describe())
print("\n", temperatures.head())

# Extracts the data from Mexico:
mexico = temperatures.loc[temperatures["Area"] == "Mexico"]

# Extracts the columns between "Y1961" and "Y2019":
mexico = mexico.loc[:, "Y1961":]
print(mexico)

# Fills "x" list values for years:
x = list(range(1961, 2019+1))
y = []
# Fills "y" list values for average of temperature changes on the year:
for year in x:
    year_temps = np.array(mexico[f"Y{year}"])
    y.append(np.average(year_temps))


# Applies a Linear Regression to the average temperatures increments:
regression = LinearRegression()
x = np.array(x)
x = x.reshape(-1, 1)
regression.fit(x, y)

# Plots the info:
plt.suptitle("Mexico Temperature Increments")
plt.title("Since 1961 to 2019")
plt.xlabel("Year")
plt.ylabel("Temperature increment (°C)")
plt.plot(x, y, color="blue")
plt.plot(x, regression.predict(x), color="red")
plt.legend("°")
plt.show()