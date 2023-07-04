import pandas as pd
from sklearn.linear_model import LinearRegression

auto = pd.read_csv("../Dataset/clean_auto.csv")

regression = LinearRegression()

x = auto[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
Y = auto["price"]

regression.fit(x.values, Y)
print("\nINTERCEPT:", regression.intercept_)
print("COEFFICENTS:", regression.coef_)

y_prediction = regression.predict(x)
print("PREDICTIONS:\n", y_prediction)

print("\nPrediction based on:")
horsepower = float(input(" * Horsepower: "))
curb_weight = float(input(" * Curb Weigth: "))
engine_size = float(input(" * Engine Size: "))
highway_mpg = float(input(" * Highway MPG: "))
predicted_price = regression.predict([[horsepower, curb_weight, engine_size, highway_mpg]])
print(f"\nPREDICTED PRICE: ${predicted_price[0]:.2f}\n")