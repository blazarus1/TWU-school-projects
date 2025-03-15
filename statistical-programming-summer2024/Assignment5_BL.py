# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 5
# source: Week 6 Recordings

#####################################################################

# import appropriate packages
import pandas as pd
import scipy.stats

# function for anova test
def anova_test():
    # reading text file, tab delimited, with UTF-16 encoding
    df = pd.read_csv("calvs_weights.txt", encoding='UTF-16 LE', sep='\t')
    #print(df)
    # printing the descriptive statistics for each column, or group, of Feeds
    print(df.describe())

    # Null hypothesis: mean_Feed1 = mean_Feed2 = mean_Feed3 = mean_Feed4
    # Alternative hypothesis: not all means are equal
    # setting alpha level
    alpha = 0.05

    # converting each column, or group, to a list using the iloc function
    Feed1 = df.iloc[:,0].to_list()
    Feed2 = df.iloc[:,1].to_list()
    Feed3 = df.iloc[:,2].to_list()
    Feed4 = df.iloc[:,3].to_list()

    # using f_oneway() from scipy.stats to get results
    results = scipy.stats.f_oneway(Feed1, Feed2, Feed3, Feed4)
    print('F-statistic: ', results.statistic)
    print('p-value: ', results.pvalue)

    # using p-value to reject or fail to reject the null, where rejection happens when p-value < alpha
    if results.pvalue < alpha: 
        print("Reject Null Hypothesis")
    else:
        print("Fail to reject Null Hypothesis")


# entry point - main program
if __name__ == "__main__":
    anova_test()