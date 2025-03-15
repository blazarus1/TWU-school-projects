# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 3
# source:
# source:

#####################################################################

# import appropriate packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# pearson correlation coefficient formula

# reading in file from current directory into a pandas dataframe
fn = "StudentsPerformance.csv"
df = pd.read_csv(fn)
x = df["reading score"].to_numpy()
y = df["writing score"].to_numpy()

x_mean = np.mean(x)
y_mean = np.mean(y)

s_1 = 0
for item in x:
    s_0 = (item - x_mean)
    