import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score

# Getting the Boston Housing Prices Dataset:
auto = pd.read_csv("../Dataset/clean_auto.csv")
X = auto[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
y = auto["price"]

# Creating a Polynomio of degree 2 based on x data:
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Creates a Linear Regression and train it with Poly-X data:
model = LinearRegression()
model.fit(X_poly, y)

# Creates the points of lines of the regression:
#? X_lines is a division of 100 points between the data, to delimitate the
X_line = np.linspace(np.min(X), np.max(X), 100)
X_line_poly = poly_features.fit_transform(X_line)
y_line = model.predict(X_line_poly)

#/ Prints the Regression model data:
print(f"\n* Coefficent: {model.coef_}")
print(f"* Intercept: {model.intercept_}")
print(f"* Precision: {model.score(X_poly, y)*100:.4f}%")
scores = cross_val_score(model, X_poly, y, scoring="r2", cv=4)
print(f"* Cross-Validation Precision List: {scores}")
print(f"* Cross-Validation Precision: {np.mean(scores)*100:.4f}%\n\n")