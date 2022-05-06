# -*- coding: utf-8 -*-
"""
Class Notes 12 April 2022
Nathaniel Gunter
"""

import timeit

# Handle imports
import numpy as np
from matplotlib import pyplot as plt

# import iris data
iris_data = np.loadtxt('./iris_dataset.txt')

"""
Last time: Finished with accessing rows and copies of arrays
"""

"""
Subarrays as no-copy views
"""

x = iris_data[2:5, 0:2]
print(x)

x[0, 0] = 100
print(x)

print(iris_data)

# This edits the original data, ie doesn't create a copy in a new memory space

x = iris_data[2:5, 0:2].copy()
print(x)

x[0, 0] = 100
print(x)
print(iris_data)
# .copy() creates a new copy in memory

"""
Loops on NumPy arrays
"""
"""
Ex: Compute reciprocals of the values in an array using a loop
"""


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


big_array = np.random.randint(1, 100, size=1000000)

# t = timeit.timeit('compute_reciprocals(big_array)', globals=globals(), number=1)
# print('Loop was executed in', t, 'seconds.')

"""
Loops on NumPy arrays are SLOW!

This is partly due to the dynamic, interpreted nature of the language: the fact that types are flexible, so that
sequences of operations cannot be compiled for efficiency as in C and Fortran. 

Instead use vectorized operations
"""

"""
Vectorized operations

-This can be accomplished simply by performing an operation on the array

-Vectorized operations are implimented via ufuncs, whose main purpose is to quickly execute repeated actions
"""

t = timeit.timeit('1/big_array', globals=globals(), number=1)
print('Vectorized operation executed in', t, 'seconds.')

"""
NumPy arrays arithmetics
"""

x = np.arange(4)
print("x = ", x)

# Exercise: Figure out what the following do

print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
# *, /, // (floor division), -x, ** (exponent), % (modulus)

# Standard order of operations is respected

# This converts '5' to a vector with each element as 5

x[3] = x[3] / 2  # Returns 1, not 1.5, because np.array can only hold one type (in this case integers)

# The same operations can be used on two NumPy arrays, these run elementwise (requires identical size)

# Absolute values (numpy version np.abs() is faster than abs())

"""
Computations on Arrays: Broadcasting
"""
a = np.arange(3)
print(a + 5)

a = np.arange(3)
m = np.ones((3, 3))
print(m + a)

# Before addition, considers dimensions. m(3,3) and a(3). For a visual representation of what happens, see slides
#   from today.

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print(a)
print(b)
print(a + b)

"""
Rules of Broadcasting

1. If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with
    ones on its leading (left) side)
2. If the shape of the two arrays does not match in any dimension, the array with shape TODO: Finish this from slide"""

"""
Trigonometric functions, Exponentials, and Logarithms

np.sin(), np.tan(), etc.

How can we plot y = cos(x) on interval [0, 10]?
    Cannot evaluate cos(x) for all reals on [0,10], choose enough equally spaced numbers to approximate
"""

x = np.linspace(0, 10, 1000)
y = np.cos(x)

plt.plot(x, y)

# No axis labels yet

plt.title('y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')

# Save the figure on the computer

plt.savefig('foo.png')


"""
Aggregates

- For binary ufuncs, ther e are some interesting aggregates that can be computed directly from the object
- For example, if we'd like to reduce an array with a particular operation, we can use the reuce method of a ufunc
- Reduce repeatedly applies a given operation to the elements of an array until only a single result remains
"""

x = np.arange(1,6)
print(np.add.reduce(x))
print(np.multiply.reduce(x))

# If we want to store intermediate steps, use .accumulate() instead of .reduce()
print(np.add.accumulate(x))
print(np.multiply.accumulate(x))

# Compute the inner product of the vectors v1 + v2

v1 = np.arange(2,101)
v2 = np.arange(98,-1,-1)
# OR use v2 = np.arange(99)[::-1]
print(np.add.reduce(v1*v2))
# Check with the actual dot product function
print(np.dot(v1, v2))

"""
x = np.arange(10)
sum() exists, but np.sum() or x.sum() is faster
"""

M = np.random.randint(1,10,(3,4))
print(M)
print(M.sum())
print(M.sum(axis = 0))
print(M.sum(axis = 1))

# NumPy provides other agregatation functions (check documentation or slides)