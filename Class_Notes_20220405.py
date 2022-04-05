# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:16:09 2022

@author: Nathaniel Gunter
"""

## Class Notes & Workbook 5 April 2022 ##

# Homework Submissions: Single .py file to be submitted with both functions and test code
#   Test code: 2-3 test cases, as varied as possible

# Final Project: Groups of two people max
#   Clustering algorithms: Choose a clustering method
    #   Mathematical background
    #   Implementation
    #   Application to a data set
#   More to come on Canvas

# Public talk today, 5:30 pm PHSC 201
#   Dr. Konstantin Mishaikow: We have Data and Computers, why do we need Math?

##  Introduction to NumPy Arrays and Datasets

# First dataset (Iris Dataset)
#   - Part of the Seaborn Library
#   - Contain four features: length and width of sepals and petals in cm of
#       three species of Iris (Iris Setosa, Iris Verginica, and Iris Versicolor)
#   - Data typically stored as matrix:
    #   - Rows = individual plants that were measured
    #   - Columns = correspond to different measurements
#   - A 'data matrix' is a matrix which stores data
#   - The 'observations', which are also known as cases, are stored as rows
    #   within the data matrix
#   - The 'variables' are stored as columns

# NumPy Arrays
#   - Data manipulation == NumPy array manipulation
#   - NumPy is constrained to arrays where all entries are of the same type
#   - Newer tools (see 'Pandas') are built on NumPy arrays

# Creating Arrays from Lists:
    # Example 1:
# Import numpy in order to use numpy tools
import numpy as np
x = np.array([1,3,5,2,1])
print(x)

# Example 2
x = np.array([1.7, 3, 5, 2, 1])
print(x)

#   - If types do not match, NumPy wil upcast if possible (here int to float)

#Example 3
x = np.array([1.7,3,5,2,'a'])
print(x)

#   - Here everything is upcast to strings. we cannot do any arithmetic
    #   operationns on x.

# Matrix example
x = np.array([[1,2,3],[4,5,6]])
print(x)

## Exercise 1: Create a one dimensional integer array of length 500 filled
#   with zeros

x = np.zeros(500, dtype = int)
print(x)
# Note also that multiplying a list by an integer concatenates it with itself that
#   many times.

# Exercise 2: Create a matrix with 3 rows and 5 columns filled with zeros

x = np.zeros([3,5], dtype = int)
print(x)

# Exercise 3: Create a 4x6 floating-point array filled with 1s

x = np.ones((4,6), dtype = float)
print(x)

# Exercise 4: Create a 2x3 array filled with 3.14
x = np.full((3,2), 3.14)
print(x)

# Exercise 5: Create a 3x3 array of random integers in the interval [0,1)

x = np.random.random((3,3))
print(x)

# Exercise 6: Create a random 3x2 array of integers in the interval [0,10)

x = np.random.randint(0,10,(3,2))
print(x)

# Exercise 7: Create a 4x4 identity matrix

x = np.eye(4)
print(x)

# Exercise 8: Creat an array 10 values evenly spaced between 0 and one
x = np.linspace(0,1,10)
print(x)

# Load Iris Dataset from a Text File
#   - Download from web, converted s.t. 'Setosa =1', 'versicolor' = 2, 
    #   'virginica' = 3
#   - Columns separated by an empty space, rows separated by newlines

# Load the dataset
iris_data = np.loadtxt('./iris_dataset.txt')
print(iris_data)

# Check the number of rows and columns
iris_dim = iris_data.ndim
iris_shape = iris_data.shape
iris_size = iris_data.size
print('There are', iris_shape[1], 'columns and', iris_shape[0], 'rows.')
print('Furthermore, the data has', iris_dim, 'dimensions and', iris_size, 'elements.')

x = np.linspace(0,1,10)
#Exercise: print the fifth entry of vector x

print(x[4])

#Exercise: print the last entry of the vector x

print(x[-1])

#Exercise: What if you do not know the number of elements in x?

print('The above still works because it wraps around backwards.')

#Exercise: print the circled entry from the iris_data matrix (2,3)

print(iris_data[1,2])

#Array slicing
#   - x[start:stop:step]

print(x[:5])
print(x[-4:])

#Exercise: print elements after index 5, including 5
print(x[5:])

#Exercise: print elements with indices 4-7
print(x[4:8])

#Exercise: print every other element starting at index 1

print(x[1::2])

#Exercise: Print elements in a reversed order

print(x[::-1])

# Accessing array rows and columns
#   - print(iris_data[0,:]) gives the first row of the dataset

# Exercise: Print the second column of iris_data
print(iris_data[:,1])

# Exercise: print the marked part of the matrix iris_data

print(iris_data[2:5, 1:])

# Next time: More about matrices and copies of arrays