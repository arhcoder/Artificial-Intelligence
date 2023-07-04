# ANALYSIS OF VARIANCE #
#? It is to find correlation between different groups of a categorical variable.

import pandas as pd
from scipy import stats

auto = pd.read_csv("../Dataset/clean_auto.csv")
# print(auto.describe())

df_anova = auto[["make", "price"]]
grouped_anova = df_anova.groupby(["make"])
# print(grouped_anova)

# ANOVA Between honda and Subaru:
anova_results = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("subaru")["price"])
print(anova_results)

# ANOVA Between honda and Jaguar:
anova_results = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("jaguar")["price"])
print(anova_results)