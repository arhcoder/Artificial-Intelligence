import pandas as pd
from scipy import stats

#/ PEARSON CORRELATION /#

#? Two values:

    #* Correlation coefficent:
        #! Close to +1: Large Positive Relationship.
        #! Close to -1: Large Negative Relationship.
        #! Close to  0: No Relationship.
    #* P-Value:
        #! P-Value < 0.001: Strong certainty in the result.
        #! P-Value < 0.05:  Moderate certainty in the result.
        #! P-Value < 0.1:   Weak certainty in the result.
        #! P-Value > 0.1:   NO certainty in the result.

    #/ STRONG CORRELATION when:
    #/  Correlation coefficent close to 1 or -1.
    #/  P Value less than 0.001.

auto = pd.read_csv("../Dataset/clean_auto.csv")

pearson_coef, p_value = stats.pearsonr(auto["horsepower"], auto["price"])

# 0.8096068016571054 6.273536270650436e-48;
# STRONG CORRELATION:
print(pearson_coef, p_value)