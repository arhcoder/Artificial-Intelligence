import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

auto = pd.read_csv("../Dataset/clean_auto.csv")

# Plots the relation between engine-size and price:
sns.regplot(x="engine-size", y="price", data=auto)
# Puts a regression line:
plt.ylim(0,)
plt.show()

# Plots the relation between highway-mpg and price:
sns.regplot(x="highway-mpg", y="price", data=auto)
# Puts a regression line:
plt.ylim(0,)
plt.show()