# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 6
# source: Week 7 Recordings
# chatGPT and geeksforgeeks.com for hypothesis testing help with t-statistic and critical value

#####################################################################

# import appropriate packages
import pandas as pd
from scipy.stats import norm, zscore, pearsonr, spearmanr, t
from sklearn import preprocessing, linear_model, metrics
import matplotlib.pyplot as plt
import numpy as np

# reading in data
df = pd.read_csv("Real_Estate.csv")

# EXPLORATORY DATA ANALYSIS
print(df.head(10))
print(df.info())

# printing descriptive stats of numerical columns
print(df.describe())

# PREDICTIVE HYPOTHESES - distance to nearest MRT station and price
# null hypothesis: distance to station does not predict price
# alternative hypothesis: distance to station does predict price

stations = df["Distance to the nearest MRT station"].values.reshape(-1,1)
price = df["House price of unit area"].values.reshape(-1,1)

plt.scatter(stations,price)
plt.show()


# showing histograms
title1 = "Distance to station"
plt.hist(stations)
plt.title(title1)
plt.show()
title2 = "House price"
plt.hist(price)
plt.title(title2)
plt.show()

# transform using z score
stations = zscore(stations)
price = zscore(price)
    
# fitting the normal distribution to data with mean and standard deviation
mean, sd = norm.fit(stations)
# plotting the histogram with 100 bins, from lecture
hist, bins = np.histogram(stations)
plt.bar(bins[:-1], hist)

# plotting the normal distribution with the norm.pdf function with data, mean and standard deviation
p = norm.pdf(stations, mean, sd)
plt.plot(stations, p)
# showing results in the title of the plot with f strings
title3 =  "Stations " + "Results: mean = %.2f, sd = %.2f" % (mean, sd)
plt.title(title3)
plt.show()

# fitting the normal distribution to data with mean and standard deviation
mean2, sd2 = norm.fit(price)
# plotting the histogram with 100 bins, from lecture
hist, bins = np.histogram(price)
plt.bar(bins[:-1], hist)

# plotting the normal distribution with the norm.pdf function with data, mean and standard deviation
p = norm.pdf(price, mean, sd)
plt.plot(price, p)
# showing results in the title of the plot with f strings
title4 =  "Price " + "Results: mean = %.2f, sd = %.2f" % (mean, sd)
plt.title(title4)
plt.show()

# using correlation to compare variables
# using ravel() as reshaping/flattening array
r = pearsonr(np.ravel(stations), np.ravel(price))
print(f"pearson correlation cofficient is {r.statistic}")
print(f"p-value is {r.pvalue}")
# using r squared to determine explanation of variations
r_squared = float(r.statistic) * float(r.statistic)
print(f"r squared is {r_squared}")

# hypothesis testing for r
# null hypothesis h_0: there is no linear relationship between the two variables, thus r = 0
# null hypothesis h_1: there is a linear relationship between the two variables, thus r != 0
# degrees of freedom, alpha level, and critical value
n = len(stations)
degrees_freedom = n - 1
alpha = 0.05
critical_value = t.ppf(1 - alpha/2, degrees_freedom)

# test statistic
t_statistic = r.statistic * np.sqrt((n - 2) / (1 - r.statistic**2))
print(f"t-statistic is {t_statistic}")
print(f"t-critical value is {critical_value}")

# decision for hypothesis test
if abs(t_statistic) > critical_value:
    print("reject the null hypothesis")
else:
    print("fail to reject the null hypothesis")

if r.pvalue < 0.05:
    print("reject the null hypothesis")
else:
    print("fail to reject the null hypothesis")

# training model on 80% of the data
stores_train = stations.ravel()[0:330].reshape(-1,1)
stores_test = stations.ravel()[330:413].reshape(-1,1)
price_train = price.ravel()[0:330].reshape(-1,1)
price_test = price.ravel()[330:413].reshape(-1,1)

# LINEAR REGRESSION
regression = linear_model.LinearRegression()
regression.fit(stores_train,price_train)

price_prediction = regression.predict(stores_test)

# prediction of accuracy - need small number for high accuracy
accuracy = metrics.mean_squared_error(list(price_test.ravel()), list(price_prediction.ravel()))
print(f"accuracy of least squares regression line is {accuracy}")

# plotting the fit line to the scatter plot of the columns
plt.scatter(stations,price)
plt.plot(stores_test, price_prediction, color = "blue", linewidth=3)
plt.show()


# transform using min max
# scaler = preprocessing.MinMaxScaler()
# stations = scaler.fit_transform(stations)
# price = scaler.fit_transform(price)


# calculating spearman's rank correlation
# r_s = spearmanr(stations, price)
# print(f"spearman rank correlation coefficient is {r_s.statistic}")
# print(f"p-value is {r_s.pvalue}")