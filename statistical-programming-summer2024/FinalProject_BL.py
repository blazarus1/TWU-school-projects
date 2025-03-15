# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Final Project
# source: https://realpython.com/logistic-regression-python/
# source: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
# source: https://www.analyticsvidhya.com/blog/2022/09/dealing-with-outliers-using-the-iqr-method/

#####################################################################

# IMPORT APPROPRIATE PACKAGES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# READING DATA
df = pd.read_csv("Breast_cancer_data.csv")

# BEGINNING EXPLORATORY DATA ANALYSIS
print(f"DESCRIPTIVE STATISTICS \n {df.describe()} \n")
print(f"FIRST TEN ROWS OF DATAFRAME \n {df.head(10)} \n")
print(f"INFORMATION ABOUT COLUMNS \n {df.info()} \n")

# checking for null values
print(f" \n {df.isnull().sum()} \n")

# GRABBING VALUES OF COLUMNS
area = df["mean_area"].values
smooth = df["mean_smoothness"].values

# PLOTTING HISTOGRAMS
plt.hist(area)
plt.show()
plt.hist(smooth)
plt.show()

# scatter plot to compare the independent variables
plt.scatter(area, smooth)
plt.xlabel("Area")
plt.ylabel("Smooth")
plt.show()

# box plot to check for outliers
plt.boxplot(area)
plt.title("Area")
plt.show()
plt.title("Smooth")
plt.boxplot(smooth)
plt.show()

# DEALING WITH OUTLIERS USING IQR METHOD
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
no_outliers = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]


# GRABBING VALUES OF COLUMNS AFTER IMPUTING OUTLIERS WITH IQR METHOD
# creating 2-D numpy array for correct input into logistic regression model
area = no_outliers[["mean_area"]].to_numpy()
# print(area.shape)

smooth = no_outliers[["mean_smoothness"]].to_numpy()
# print(smooth.shape)

diagnosis = no_outliers["diagnosis"].to_numpy()

# instantiation of the class StandardScaler
scaler = StandardScaler()
# scaling the explanatory variables
area_scaled = scaler.fit_transform(area)
smooth_scaled = scaler.fit_transform(smooth)

# showing boxplots without outliers and scaled data
plt.boxplot(area_scaled)
plt.title("Area")
plt.show()
plt.title("Smooth")
plt.boxplot(smooth_scaled)
plt.show()

def logistic_regression (X, y):
# # simple logistic regression

    # instantiation and fitting of model
    model = LogisticRegression(solver='liblinear', random_state=0)
    model.fit(X,y)

    # PRINTING RESULTS
    print(f"THESE ARE THE SIMPLE REGRESSION RESULTS")
    print(f'Binary Classifiers: {model.classes_}')
    print(f'Intercept: {model.intercept_}')
    print(f'Coefficent: {model.coef_}')
    print(model.predict_proba(X[2:6]))
    print(model.predict(X[2:6]))
    print(f'Model Score: {model.score(X,y)}')
    print(f'Confusion Matrix:\n {confusion_matrix(y, model.predict(X))}')
    print(f'Classification Report:\n {classification_report(y, model.predict(X))}')

# calling function with input parameters X and y
logistic_regression(area_scaled, diagnosis) 
logistic_regression(smooth_scaled, diagnosis)


# MULTIPLE LOGISTIC REGRESSION WITH TWO EXPLANATORY VARIABLES

# stack columns of np arrays into 2D array and throw in X input variable
X = np.column_stack((area_scaled, smooth_scaled))
# declare y classification variable
y = diagnosis

# fit model with multiple input variables and y variable
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X,y)

# PRINTING RESULTS
print("THESE ARE THE MULTIVARIATE RESULTS")
print(f'Binary Classifiers: {model.classes_}')
print(f'Intercept: {model.intercept_}')
print(f'Coefficent: {model.coef_}')
print(model.predict_proba(X[2:6]))
print(model.predict(X[2:6]))
print(f'Model Score: {model.score(X,y)}')
print(f'Confusion Matrix:\n {confusion_matrix(y, model.predict(X))}')
print(f'Classification Report:\n {classification_report(y, model.predict(X))}')