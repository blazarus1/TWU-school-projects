# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 1
# source: https://www.geeksforgeeks.org/how-to-plot-a-normal-distribution-with-matplotlib-in-python/

############################################################################################################################

# importing matplotlib (for plotting), numpy (for arrays), scipy(for normal dist.), and statistics(for mean and sd)
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics as stats

# Creating 3 different sequences numbers to plot on x-axis of normal distribution, each sequence steps by 0.1
x_1 = np.arange(-10, 10, 0.1)
x_2 = np.arange(-5, 5, 0.1)
x_3 = np.arange(-2, 2, 0.1)

# creating function to draw normal distribution
def normal_distribution(input):
    #the stats class can calculate the mean for given sequence
    mean = stats.mean(input)
    # the stats class can calculate the standard deviation for given sequence
    sd = stats.stdev(input)
    
    # Using f-strings to print mean and standard deviation
    print(f"The mean is {mean}")
    print(f"The standard deviation is {sd}")
    
    # Drawing normal distribution with user-defined input, norm class from scipy with parameters of user-defined sequence, mean, and standard deviation calculated from function
    plt.plot(input, norm.pdf(input, mean, sd))
    plt.show()
    
    
# Calling function for three different user-defined sequences
normal_distribution(x_1)
normal_distribution(x_2)
normal_distribution(x_3)