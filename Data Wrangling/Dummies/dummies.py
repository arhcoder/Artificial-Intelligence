import pandas as pd
import numpy as np

temps = pd.read_csv("../Dataset/Temperatures/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")

#/ "GET DUMIES" create a new data frame converting categorial variables on numerical; as this:
'''
    If we have data with columns "Area" like this:

    Area

    Mexico
    Mexico
    Brazil
    Argentina
    Chile
    Chile
    Chile
    Chile
    USA

    It creates a table with 1 or 0 if a row has or not each of the "Areas"; eg:

    Mexico      Brazil      Argentina       Chile       USA
    1           0           0               0           0
    1           0           0               0           0
    0           1           0               0           0
    0           0           1               0           0
    0           0           0               1           0
    0           0           0               1           0
    0           0           0               1           0
    0           0           0               1           0
    0           0           0               0           1

'''
dummies = pd.get_dummies(temps["Area"])

print(dummies.head())