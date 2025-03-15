# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 3
# source: Week 4 Recordings and Week 5 Recordings

#####################################################################

# import appropriate packages
import pandas as pd
import numpy as np

# reading in file from current directory into a pandas dataframe
fn = "StudentsPerformance.csv"
df = pd.read_csv(fn)

# converting reading and writing scores to numpy arrays
x = df["reading score"].to_numpy()
y = df["writing score"].to_numpy()

# create function to calculate pearson correlation coefficient, with parameters as arrays on x and y axis (reading and writing scores in this case)
# must be numpy arrays
def pearson_cc(x, y):

    # Calculate the means of x and y arrays
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Calculate the numerator and denominator of the Pearson correlation coefficient formula using sum() for summing all x-x-bar values and y-y-bar values
    num = np.sum((x - x_mean) * (y - y_mean))
    denom = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    
    # Calculate the Pearson correlation coefficient, denoted by r
    r = num / denom
    
    print(f"The Pearson Correlation Coefficient is {r}")

# call the function
pearson_cc(x, y)

