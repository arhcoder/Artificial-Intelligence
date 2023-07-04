import pandas as pd
import numpy as np

# Example to formatting temperature in C to F:

df = pd.read_csv("../Dataset/Temperatures/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")

#? Gets the mean of temperature on 1961:
mean_1961 = df["Y1961"].mean()

#? Replace all missing values on 1961 with the mean:
df["Y1961"].replace(np.nan, mean_1961, inplace=True)

#? Converts all temperatures from C to F:
df["Y1961"] = (df["Y1961"] * (9/5)) + 32

#? Rename the column name:
df.rename(columns={"Y1961": "Y1961-F"}, inplace=True)

#? Converts the column datatype to float (not necessary but illustrative):
df["Y1961-F"] = df["Y1961-F"].astype("float")

#? Prints the temperatures:
temps_1961 = df["Y1961-F"]
# for temp in temps_1961:
#    print(temp)

# Printing the result:
print(df.info())
print(df.loc[:, "Y1961-F":].describe())