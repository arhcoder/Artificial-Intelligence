import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

auto = pd.read_csv("../Dataset/clean_auto.csv")

lr = LinearRegression()
x = auto[["highway-mpg"]]
y = auto["price"]

lr.fit(x, y)
print("\nINTERCEPT:", lr.intercept_)
print("COEFFICENTS:", lr.coef_)

y_prediction = lr.predict(x)
print("PREDICTIONS:\n", y_prediction)

sq_error = mean_squared_error(auto["price"], y_prediction)
print("MEAN SQUARED ERROR:", sq_error)
print(f"PRECISION: {(lr.score(x, y)*100):.4f}%")

plt.suptitle("LINEAR REGRESSION WITH CARS INFORMATION")
plt.title("For Highway MPG vs Price")
plt.xlabel("Highway MPG")
plt.ylabel("Price")
plt.scatter(x, y, c="blue")
plt.plot(x, lr.predict(x), color="red")
plt.show()