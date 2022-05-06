# -*- coding: utf-8 -*-
"""
Lab 3
Due May 6
Nathaniel Gunter
"""

"""
Handle Imports
"""

import numpy as np

"""
Problem 2: Implement the formulas (worked out in the theory section).
"""


# The problem as stated in number 1 was to find the coefficients, which, while close to finding the best fit, is easier
#   to test.

def build_equations(x, y):
    """

    :param x: feature matrix
    :param y: target vector
    :return:
        matrix - matrix of normal equations
        b - rhs of normal equations
    """
    # Start by appending a column of ones to the left of the matrix of x values (this gives something for a_0 values to
    # latch onto).
    phi = np.append(np.ones((np.shape(x)[0], 1)), x, axis=1)

    # Now compute phi_t * phi
    matrix = np.matmul(np.transpose(phi), phi)

    # And compute phi_t * y
    b = np.matmul(np.transpose(phi), y)

    return matrix, b


# Now apply the above to actually calculate the coefficients
def multiple_linear_fit(x, y):
    """

    :param x: the matrix of observation variables
    :param y: the vector of response variables
    :return:
        a: the vector of coefficients for a fit of the form y = a_0 + a_1 * x_1 + ... + a_m * x_m
    """

    # Find the normal equations
    [matrix, b] = build_equations(x, y)
    a = np.linalg.lstsq(matrix, b, rcond=None)
    return a


"""
Problem 3: Test your implementation
"""


# Build a set of synthetic data dependent on multiple observation variables to test the implementation on
def make_data(N, err=1.0, rseed=1):
    """

    :param N: the number of datapoints to generate
    :param err:
    :param rseed:
    :return:
        X - An array of observation variables with three columns and N rows
        y - a vector of response variables N long
    """
    rng = np.random.RandomState(rseed)
    x1 = rng.randn(N)
    x2 = rng.randn(N)
    x3 = rng.randn(N)
    X = np.transpose(np.array([x1, x2, x3]))
    y = 0.7 + x1 + (3.5 * x2) - (3 * x3)
    if err > 0:
        y += err * rng.randn(N)
    return X, y


# start by testing for the example with no error
[x_clean, y_clean] = make_data(20, 0)

coeffs_clean = multiple_linear_fit(x_clean, y_clean)
print("Testing fit function on data with no introduced error first. Expect to get coeffs = [0.7, 1, 3.5, -3].")
print("Tested and got", coeffs_clean[0])

# Now test on data with error
[x_dirty, y_dirty] = make_data(20, 0.5)

coeffs_dirty = multiple_linear_fit(x_dirty, y_dirty)
print(
    "Testing fit function on data with no introduced error first. Expect to get something approaching coeffs = [0.7, 1, 3.5, -3].")
print("Tested and got", coeffs_dirty[0])

print("Does this get better with more data?")
[x_long, y_long] = make_data(200, 0.5)
coeffs_long = multiple_linear_fit(x_long, y_long)
print("Fitting returns", coeffs_long[0], " for 200 data points instead of 20.")

"""
Problem 4: Use your code to find the best fit for the data stored in the file 'data_8dimensions.txt'. Interpret
    the first seven columns as x**1, x**2, ... , x**7, and the last column as y.
"""

# Load in the data
dat8d = np.loadtxt('./data_8dimensions.txt')
dat8d_x = dat8d[:, :7]
dat8d_y = dat8d[:, -1]

# Find the coefficients
fit8d = multiple_linear_fit(dat8d_x, dat8d_y)
print("According to the fitting functions, the coefficints for the eight dimensional data are", fit8d[0])
ystr = ""
for i in range(len(fit8d[0])):
    if i ==0:
        ystr += str(fit8d[0][0]) + " + "
    elif i<7:
        ystr += str(fit8d[0][i]) + " * x" + str(i) + " + "
    else:
        ystr += str(fit8d[0][i]) + " * x7"

print("Overall the fit gives y = ", ystr)