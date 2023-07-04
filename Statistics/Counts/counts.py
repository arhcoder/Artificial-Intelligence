import pandas as pd
from matplotlib import pyplot as plt
# import seaborn as sns

auto = pd.read_csv("../Dataset/clean_auto.csv")
# print(auto.describe())

# Creating a new data set counting the values of "drive-wheels" category:
drive_wheels_count = auto["drive-wheels"].value_counts()
print(drive_wheels_count)

# Ploting the count of categories:
# sns.boxplot(x="drive-wheels", y="price", data=drive_wheels_count)

# Plotting "Price"(x) vs "Engine-Size"(y):
y = auto["engine-size"]
x = auto["price"]
plt.scatter(x, y)
plt.title("Scatterplot of Engine Size vs Price")
plt.ylabel("Engine Size")
plt.xlabel("Price")
plt.show()