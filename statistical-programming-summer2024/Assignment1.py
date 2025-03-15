# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 1

############################################################################################################################

# importing matplotlib (for plotting), numpy (for arrays), scipy(for normal dist.), and statistics(for mean and sd)
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics as stats

# creating sequence of 200 numbers from -10 to 10, stepping 0.1
x_1 = np.arange(-10, 10, 0.1)
x_2 = np.arange(-5, 5, 0.1)
x_3 = np.arange(-2, 2, 0.1)


# calculating mean and standard deviation on x_axis sequence
mean_1 = stats.mean(x_1)
sd_1 = stats.stdev(x_1)

mean_2 = stats.mean(x_2)
sd_2 = stats.mean(x_2)

mean_3 = stats.mean(x_3)
sd_3 = stats.stdev(x_3)

# using pyplot and norm, while passing data, mean, and sd into norm.pdf to get normal distribution plot
plt.plot(x_1, norm.pdf(x_1, mean_1, sd_1))
plt.show()
print("The mean is " + mean_1)
print("The standard deviation is " + sd_1)

plt.plot(x_2, norm.pdf(x_2, mean_2, sd_2))
plt.show()
print(mean_2)
print(sd_2)

plt.plot(x_3, norm.pdf(x_3, mean_3, sd_3))
plt.show()
print(mean_3)
print(sd_3)