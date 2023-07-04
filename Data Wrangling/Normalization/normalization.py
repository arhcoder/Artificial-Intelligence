# NORMALIZATION TECHINQUES:

#? 1. SIMPLE FEATURE SCALING:
#* Numbers between [0 - 1]:
#/ x_new = x_old / x_max;
#! df["length"] = df["length"] / df["length"].max()

#? 2. MIN-MAX:
#* Numbers between [0 - 1]:
#/ x_new = (x_old - x_min) / (x_max - xmin);
#! df["length"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())

#? 3. Z-Score:
#* Numbers HOVER on 0 eg: [-3, 3]:
#/ x_new = (x_old - average) / standar_deviation; 
#! df["length"] = (df["length"] - df["length"].mean() / df["length"].std()