import pandas as pd
from sklearn.linear_model import LinearRegression
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

plt.suptitle("LINEAR REGRESSION WITH CARS INFORMATION")
plt.title("For Highway MPG vs Price")
plt.xlabel("Highway MPG")
plt.ylabel("Price")
plt.scatter(x, y, c="blue")
plt.plot(x, lr.predict(x), color="red")
plt.show()