# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 2
# source: https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# source: Week 3 Recordings

#####################################################################

# import appropriate packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# reading in file from current directory into a pandas dataframe
fn = "StudentsPerformance.csv"
df = pd.read_csv(fn)

# printing first 10 records of file
print(df.head(10))

# taking each column of scores from dataframe and converting each to numpy array
ms = df["math score"].to_numpy()
rs = df["reading score"].to_numpy()
ws = df["writing score"].to_numpy()

math = "math score"
reading = "reading score"
writing = "writing score"

# function for fitting and plotting the numpy arrays
def scores_distribution(input, columnName):
    # printing first 10 items in array
    print(input[0:9])
    
    # fitting the normal distribution to data with mean and standard deviation
    mean, sd = norm.fit(input)
    
    # plotting the histogram with 100 bins, from lecture
    hist, bins = np.histogram(input, bins=100)
    plt.bar(bins[:-1], hist)

    # plotting the normal distribution with the norm.pdf function with data, mean and standard deviation
    p = norm.pdf(input, mean, sd)
    plt.plot(input, p)
    # showing results in the title of the plot with f strings
    title = columnName + " " + "Results: mean = %.2f, sd = %.2f" % (mean, sd)
    plt.title(title)
    
    plt.show()
    
# calling function for 3 plots
scores_distribution(ms, math)
scores_distribution(rs, reading)
scores_distribution(ws, writing)

