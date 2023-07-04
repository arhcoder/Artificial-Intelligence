import pandas as pd
from matplotlib import pyplot as plt

auto = pd.read_csv("../Dataset/clean_auto.csv")
# print(auto.describe())

# Creates a ata frame with this three columns:
df_test = auto[["drive-wheels", "body-style", "price"]]

# Group by variables "drive-wheels" and "body-style" by average:
df_group = df_test.groupby(["drive-wheels", "body-style"], as_index=False).mean()
print(df_group)
print("\n"+"-"*40+"\n")

# Pivoting data:
df_pivot = df_group.pivot(index="drive-wheels", columns="body-style")
print(df_pivot)
print("\n"+"-"*40+"\n")

# Putting data on a heatmap:
plt.pcolor(df_pivot, cmap="RdBu")
plt.colorbar()
plt.show()