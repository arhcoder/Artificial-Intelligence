import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from matplotlib import pyplot as plt

#? Reading the dataset and extracting the important information:
auto = pd.read_csv("../Dataset/clean_auto.csv")
x = auto[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
y = auto["price"]

#! PARAMETERS OPTIONS:
parameters = [ {"alpha": [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 10000, 100000 ], "normalize": [True, False]} ]

ridge_model = Ridge()
Grid = GridSearchCV(ridge_model, parameters, cv=4)

ridge_model.fit(x.values, y)
y_prediction = ridge_model.predict(x)
print("a")

scores = Grid.cv_results_
for param, mean_val, mean_test in zip(scores["params"], scores["mean_test_score"], scores["mean_train_score"]):
    print(param, "R^2 on test data:", mean_val, "R^2 on train data:", mean_test)

print("\nINTERCEPT:", ridge_model.intercept_)
print("COEFFICENTS:", ridge_model.coef_)

y_prediction = ridge_model.predict(x)
print("PREDICTIONS:\n", y_prediction)