# Bethany Lazarus
# CSCI 5663 Statistical Programming
# Assignment 4
# source: Week 5 Recordings

#####################################################################

# import appropriate packages
import math as m

# n choose k = n! / k!*(n-k)!
# binomial distribution formula = (n choose k) * (p**k) * ((1-p)**n-k)

# probability of flipping 7 out of 10 heads given the p=0.8 for heads
# n = 10, k = 7, p = 0.8, q=0.2 (also 1-p)

def binomial_prob (n, k, p):
    # choose formula
    n_choose_k = m.factorial(n) / (m.factorial(k) * m.factorial(n-k))
    # second part of formula
    prob_of_success = p**k
    # third part of formula
    prob_of_failure = (1-p)**(n-k)

    # putting them all together
    bin_distr_prob = n_choose_k * prob_of_success * prob_of_failure
    
    # print results and problem out for user
    print(f"The probability of getting {k} successes out of {n} trials is, given the success rate of {p}, is {bin_distr_prob}")

# calling function
binomial_prob(10, 7, 0.8)