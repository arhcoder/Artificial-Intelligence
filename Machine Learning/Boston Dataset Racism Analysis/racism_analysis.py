'''
    ABOUT THIS PROJECT:

    While I was doing exercises to practice linear and polynomial regression, I came across exercises in
    which a dataset about the price of rent in Boston is used. I got an initial error, because apparently
    the scikit-learn library withdrew said dataset a long time ago due to lack of ethics in it.

    After digging a bit in the dataset, I find that there is a variable named "B", which indicates the
    portion of the Afrincan American community. Reading:
    medium.com/@docintangible/racist-data-destruction-113e3eff54a8.

    I'll try to do some analysis to understand why a variable like "B" would be included in such a dataset,
    and what implications it has for the entire dataset.
'''

#? Libraries:
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
import statsmodels.api as sm


#? Reading the Boston Housing Dataset:
boston = pd.read_csv("../Dataset/boston_housing_corrected.csv")
print(boston.describe())
print("\n"+"-"*60+"\n")


#? Plotting the relation between "B" and "MEDV" (price of housing):
x = boston[["B"]]
y = boston["CMEDV"]

regression = LinearRegression()
regression.fit(x, y)

plt.suptitle("HOUSING PRICE IN BOSTON")
plt.title("African American Population vs Housing Price")
plt.scatter(x, y)
plt.xlabel("African American Population (1000(Bk - 0.63)^2)")
plt.ylabel("Housing Price ($1000's)")
plt.plot(x, regression.predict(x), color="red")
plt.show()

'''
    There's no correlation; there are not enogh information to
    identify correlation between two separate variables.
'''


#? Binning based on amount of "B":
bins = np.linspace(min(boston["B"]), max(boston["B"]), 6)
groups = ["Lowest", "Low", "Medium", "High", "Highest"]
boston["B-Binned"] = pd.cut(boston["B"], bins, labels=groups, include_lowest=True)
print(boston[["B", "B-Binned"]])

amounts = [0, 0, 0, 0, 0]
for town in boston[["TOWN", "B-Binned"]].values:
    if town[1] == "Lowest":
        amounts[0] += 1
    elif town[1] == "Low":
        amounts[1] += 1
    elif town[1] == "Medium":
        amounts[2] += 1
    elif town[1] == "High":
        amounts[3] += 1
    elif town[1] == "Highest":
        amounts[4] += 1

print(f"\n{groups}")
print(amounts)
print("\n"+"-"*80+"\n")

plt.suptitle("Communities with \"highest\" concentration of African American population in Boston")
plt.title("Based on Boston Housing Dataset from 1978 to 1997 \"B\" variable")
plt.xlabel("African American portion")
plt.ylabel("Amount of towns")
plt.bar(groups, amounts)
plt.show()


#? ANOVA:
df_anova = boston[["B-Binned", "CMEDV"]]
grouped_anova = df_anova.groupby(["B-Binned"])

anova_results = stats.f_oneway(grouped_anova.get_group("Lowest")["CMEDV"], grouped_anova.get_group("Highest")["CMEDV"])
print("ANOVA:", anova_results)
# F_onewayResult(statistic=38.3233423832756, pvalue=1.3116657703802564e-09);

print("\n"+"-"*80+"\n")


#? PEARSON ANALYSIS:
pearson_coef, p_value = stats.pearsonr(boston["B"], boston["CMEDV"])
print("PEARSON: Correlation-Coeff:", pearson_coef, "P-Value:", p_value)
# 0.3348608318181214 1.0067475860731766e-14;

print("\n"+"-"*80+"\n")

print("THE CORRELATION BETWEEN HOUSING PRICES AND THE BLACK POPULATION IN BOSTON...")
print("IT IS LOW (33.48%), there is no correlation.")

print("\n"+"-"*80+"\n")


#? MULTIPLE REGRESSION ANAYSIS:
X_data = boston[["B", "TOWNNUM", "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "RAD", "TAX", "LSTAT"]]
target = boston["CMEDV"]

X_data = sm.add_constant(X_data)
model = sm.OLS(target, X_data).fit()

print(model.summary())

print("\n"+"-"*80+"\n")