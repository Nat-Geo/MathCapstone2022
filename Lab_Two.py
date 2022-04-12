# -*- coding: utf-8 -*-
"""
Lab 2
Due April 19
Nathaniel Gunter
"""

# Handle any necessary imports
import numpy as np

"""
Problem 1

Write a function that takes a parameter n and returns an n x n matrix that contains a checkerboard
pattern of ones and zeros. The value at the position (0,0) is 1.

Test your function for n = 3,4,10,15
"""


def checkerboard(n):
    # Define an empty matrix of the correct size
    mat = np.zeros((n, n))

    # Scan through the array, and where i+j is even, replace the zero with a one. This creates the checkerboard pattern
    #   with a one at (0,0).
    for i in range(0, n):
        for j in range(0, n):
            if (i + j) % 2 == 0:
                mat[i, j] = 1

    return mat


# Test code
print("Testing 'checkerboard()'.")

print("Testing for n = 3.")
print("Function returns:\n", checkerboard(3))

print("Testing for n = 4.")
print("Function returns:\n", checkerboard(4))

print("Testing for n = 10.")
print("Function returns:\n", checkerboard(10))

print("Testing for n = 15.")
print("Function returns:\n", checkerboard(15))

"""
Problem 2

Write a function that takes a one dimensional NumPy array of values that represent temperatures in
Centigrade degrees and returns an array with the corresponding temperatures in Fahrenheit degrees.

Test your function on a NumPY array with the values [1, 3.4, 75.5, 100.3, -35.2]
"""


def cent_to_faren(temps):
    ftemps = np.zeros(len(temps))
    for i in range(len(temps)):
        ftemps[i] = (temps[i] * 9 / 5) + 32
    return ftemps


# Test code
print("\n Testing 'cent_to_faren()'")
print("Testing for l = [1, 3.4, 75.5, 100.3, -35.2].")
print("Result is: \n", cent_to_faren([1, 3.4, 75.5, 100.3, -35.2]))

"""
Problem 3

Write a function that takes two NumPy arrays and returns an array that contains the common values
of the input arrays.

Test your function on NumPy arrays array1 = [1, 10, 1, 20, 4, 30, 8, 70] and array2 = [20, 10, 3, -4, 70, 80]
"""

"""
Problem 4

Write a function that takes a two dimensional  NumPy array (matrix) A and a threshold t. This function returns the 
values and indices of the elements  of A that are bigger than t.

Test your function on the matrix  A  = [[0, 10, 20], [20, 30, 40]] and t = 10
"""

"""
Problem 5

Write a function that takes a NumPy array A and returns two arrays unique_elements and counts. The array 
unique_elements contains the values of the entries of A without repetition and counts indicates how many time the 
given value is repeated. 

Test your function using A = [10 10 20 10 20 20 20 30 30 50 40 40] .

You should get the following output  unique_elements = [10, 20, 30, 40, 50] and counts = [3,4,2,2,1].
"""

"""
Problem 6

Write a function that takes two one dimensional NumPy arrays and returns their Cartesian product in a single two 
dimensional NumPy array.

Test your function using x  = [1,2,3] and y = [4,5].
"""

"""
Problem 7

Write a function that takes a two dimensional NumPy array A and returns two one dimensional NumPy arrays that contain 
the first and fourth column of A.

Test your function using a randomly generated 4 by 4 NumPy array (matrix).
"""

"""
Problem 8

Write a function that takes a NumPy array A and two real numbers min_value and  max_value. The function returns the 
values of A that are larger than min_value and smaller than max_value.

Test your function using A = [1, 3, 4, 5, 6, 7, 12, 16, 18, 32, 53],  min_value = 10 and max_value = 30.
"""

"""
Problem 9

Write a function that takes a one dimensional  NumPy array A. If the number of the elements in A is not a multiple of 3 
then the function  returns False. Otherwise the function returns a new array which contains averages of every 
consecutive triplet of elements in a given array. 

Test your function using A = [ 1 2 3 2 4 6 1 2 12 0 -12 6]
"""

"""
Problem 10

Write a function that takes a two dimensional NumPy array (matrix) A and one dimensional NumPy array (vector) b. 
It returns a one dimensional array obtained by multiplying the matrix A by the vector b.

Test your function.
"""

"""
Problem 11

Use the Iris data set (posted on canvas).  Find the maximum, minimum and mean of the petal and sepal lengths for each 
of three species of Iris.
"""

"""
Problem 12

Use the Iris data set (posted on canvas). Create a scatter plot of the sepal length and sepal width. Make sure that 
your plot contains a legend, axis labels and legend. Data points for each of the three species should be displayed 
using  different color. Is there a simple relation between sepal length and sepal width that is approximately valid for 
all specimens?
"""
