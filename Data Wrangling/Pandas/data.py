
import pandas as pd

salary = pd.read_csv("./Dataset/salary-data.csv")

salary.columns = ["Experience", "Salary"]

print("\nSalarios:")
print(salary)

print("\nCabecera:")
print(salary.head())

print("\nCola:")
print(salary.tail())

print("\nTipos:")
print(salary.dtypes)

print("\nDescripción:")
print(salary.describe(include="all"))

print("\nInfo:")
print(salary.info())