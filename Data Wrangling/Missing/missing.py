import pandas as pd
import numpy as np

temps = pd.read_csv("../Dataset/Temperatures/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")

# print("", temps.head())
# print("", temps.info())
# print("", temps.describe())

# Axis; 0 = Row; 1 = Column;
# Inplace = True; it modifies the dataframe to drop the missing data:
# temps.dropna(axis=0, inplace=True)

# Take the mean on a column to replace in missing values:
mean = temps["Y1961"].mean()
temps["Y1961"].replace(np.nan, mean, inplace=True)
t1961 = temps.loc[:, "Y1961"]
for t in t1961:
    print(t)