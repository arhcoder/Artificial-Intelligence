import pandas as pd
import numpy as np

temps = pd.read_csv("../Dataset/Temperatures/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")

# print(temps["Months"].info())
# print(temps["Months"].head())
print(temps.loc[:, "Y1961":].describe())

# The temperatures in columns from Y1961 to Y2019:
'''
            Y1961   ...       Y2019
count  8287.000000  ...  8365.000000
mean      0.402433  ...     1.094599
std       0.701567  ...     0.853953
min      -4.018000  ...    -2.644000
25%       0.057000  ...     0.455000
50%       0.366000  ...     0.939000
75%       0.676500  ...     1.508000
max       5.771000  ...     7.215000
'''

# Binning the temperatures in two categories FOR 1961:
#* ["Sub-Zero"] for temps < 0; ["Up-Zero"] for temps > 0:
groups = ["Sub-Zero", "Up-Zero"]
temps['Y1961-Binned'] = pd.cut(temps["Y1961"], [-100, 0, 100], labels=groups)

# Binning the temperatures in three categories FOR 1962:
#* ["Low", "Medium", "High"]
#! NOTE:
#? bins = np.linespace(min(prices), max(prices), 4),
#? Returs a divition of 4 - 1 equal spaces in the data range:
bins = np.linspace(min(temps["Y1962"]), max(temps["Y1962"]), 4)
new_groups = ["Low", "Medium", "High"]
temps["Y1962-Binned"] = pd.cut(temps["Y1962"], bins, labels=new_groups, include_lowest=True)

#? Prints results:
print(temps.info())
print(temps[["Y1961", "Y1961-Binned"]])
print("\n"+"-"*40+"\n")
print(temps[["Y1962", "Y1962-Binned"]])