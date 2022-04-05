# -*- coding: utf-8 -*-
"""
Lab 1
Due 12 Apr 2022
Nathaniel Gunter
"""

"""
Problem 1
Fermat's Last Theorem says that there are no positive integers a, b, and c
  such that a^n + b^n = c^n for any n greater than 2. Write a function named
  'check_fermat(a,b,c,n)' that takes four integer parameters and returns the
  following: 
  a) None - if n is not greater than 2
  b) True - if the equation is not satisfied and n is greater than 2
  c) False - if the equation is satisfied
  Try your function for different values of the parameters to make sure it
  works properly.
"""


def check_fermat(a, b, c, n):
    # First, check that n is greater than 2, otherwise return None
    if n <= 2:
        return None
    # Now, check for the truth of Fermat's theorem using the comparison
    #   operator '=='. Because we want to return True if the equation is
    #   not satisfied, use the 'not' command to flip the boolean result before
    #   returning it.
    return not ((a ^ n) + (b ^ n) == (c ^ n))


# Test cases
print("Testing cases for function 'check_fermat':")

print('Test for a = 1, b = 2, c = 3, n = 2. Expect output of None.')
print('Result is', check_fermat(1, 2, 3, 2))

print('Test for a = 1, b = 2, c = 3, n = 3. Expect output of True.')
print('Result is', check_fermat(1, 2, 3, 3))

print("There should be no case for which this function returns False, assuming that Fermat's Last Theorem is true.")

"""
Problem 2
Write a function named 'is_triangle' that takes three real numbers x, y, and
  z representing the lengths of three line segments. The function returns
  True if the line segments can form a triangle and False otherwise.
  Try your function for different values of the parameters to make sure it 
  works properly.

To have a valid triangle, the sum of any two sides must be greater than
  the third for all possible combinations. That is, we must have:
a + b > c
a + c > b
and b + c > a
"""


def is_triangle(x, y, z):
    # Each inequality gives a boolean result. By combining the inequalities
    #   using the 'and' operator, we ensure that we only return True if all
    #   three inequalities are true.
    return (x + y > z) and (x + z > y) and (y + z > x)


# Test cases
print()
print("Testing cases for function 'is_triangle':")

print('Test for x=7, y = 5, z = 10. Expect True.')
print('Result is', is_triangle(7, 5, 10))

print('Test for x=5, y = 3, z = 8. Expect False.')
print('Result is', is_triangle(5, 3, 8))

"""
Problem 3
Write a function that takes a real parameter x and prints the values x, x-1,
  x-2, ... , x-i, ... that are positive. Use the while loop.
"""


def print_decreasing_x(x):
    # First, check that x is positive to begin with
    if not x > 0:
        print('Error: Initial value of x is not greater than zero.')
        return None
    # Define a variable x_i to iterate with
    x_i = x
    n = 0
    # As long as x_i is positive, print the value, then subtract one. Also add
    # an iteration counter, as best practice for later
    while x_i > 0:
        n = n + 1
        print(x_i)
        x_i = x_i - 1
    # Returning these values allows this to serve as a calculation for n as the 
    #   floor of x, as well as calculating x_i as x mod 1.
    return x, x_i, n


# Test cases
print()
print("Testing cases for function 'print_decreasing_x'")

print('Test for x = -3.46. Expect an error.')
print_decreasing_x(-3.46)

print('Test for an integer x = 5. Expect while loop to cut before reaching 0.')
print_decreasing_x(5)

print('Test for a float x = 5.5. Expect to cut at 0.5.')
print_decreasing_x(5.5)

"""
Problem 4
One way of computing square roots is Newton's method. Suppose that you want
  to know the square root of a. If you start with almost any estimate x0, 
  you can compute a better estimate using the following iterative formula:
  x_(n+1) = (x_n+(a/x_n))/2
  Write a function which takes two parameters a and x0. This function should
  iterate the above formula until x_(n+1) = x_n for the first time, then
  returns the value of n and x_n.
  Run your function for a = 2 and x0 = 6 to make sure that it works properly.
"""


def newton_sqrt(a, x0):
    # Set an iterating variable x_n equal to the starting value
    x_n = x0
    # Initialize an iteration counter at zero iterations
    n = 0
    # Compute the first step of the convergence, x1
    x_next = (x_n + (a / x_n)) / 2
    # As long as x_n does not equal x_(n+1)
    while not x_n == x_next:
        # iterate the counter
        n = n + 1
        # set the 'current' value of x_n to the next value
        x_n = x_next
        # calculate the next iteration
        x_next = (x_n + (a / x_n)) / 2
    return n, x_n


# Test case
print()
print("Testing function 'newton_sqrt'.")

print('Test for a = 2, x0 = 6.')
res_newt = newton_sqrt(2, 6)
print('In', res_newt[0], 'iterations, converged on a value of', res_newt[1])

print('This value matches the square root of 2.')

"""
Problem 5
Write a function called 'nested_sum' that takes a list of lists of integers
  and adds up the elements from all the nested lists. Test your function
  on t = [[1,4],[3,8,3],[1],[2,-5]].
"""


def nested_sum(l):
    s = 0
    # Check to see if the input is a list or not
    if not type(l) == list:
        print('Error: Expected input to be a list.')
        return None
    # Iterate over the sub-lists inside the list t
    for i in range(len(l)):
        # Iterate over each element in the sub-list t[i]
        for j in range(len(l[i])):
            # Compute a running sum over each element
            s = s + l[i][j]
    return s


# Test case
print()
print("Testing function 'nested_sum'.")

print('Test for t = [[1,4],[3,8,3],[1],[2,-5]]. Expect a result of 17.')
print('Result is', nested_sum([[1, 4], [3, 8, 3], [1], [2, -5]]))

"""
Problem 6
Write a function called 'middle' that takes a list and returns a new list
  that contains all but the first and last elements. Try your function for
  different lists to make sure it works properly.
"""


def middle(l):
    # Check to see if the input is a list or not
    if not type(l) == list:
        print('Error: Expected input to be a list.')
        return None
    # If the list is too short to reasonably remove two elements, throw an
    #   error
    if len(l) < 2:
        print('Error: List is too short to remove two elements.')
        return None
    # Return the list t, with the first and last entries truncated. This does
    #   not modify the variable t in the process.
    return l[1:len(l) - 1]


# Test case
print()
print("Testing function 'middle'.")

print('Test for t = [1]. Expect an error')
print(middle([1]))

print('Test for t = 1. Expect an error.')
print(middle(1))

print("Test for t = ['apple','orange','banana']")
print('Result is', middle(['apple', 'orange', 'banana']))

print("Test for t = [1, 3, 2, 5, 4]")
print('Result is', middle([1, 3, 2, 5, 4]))

"""
Problem 7
Write a function called 'chop' that takes a list, modifies it by removing
  the first and last elements, and returns None. Try your function for
  different lists to make sure it works properly.
"""


def chop(l):
    # Check to see if the input is a list or not
    if not type(l) == list:
        print('Error: Expected input to be a list.')
        return None
    # If the list is too short to reasonably remove two elements, throw an
    #   error
    if len(l) < 2:
        print('Error: List is too short to remove two elements.')
        return None
    # Use 'del' to delete the first and last elements of t. This modifies the
    #   variable itself, not the output of the function
    del (l[len(l) - 1])
    del (l[0])
    return None


# Test cases
print()
print("Testng function 'chop'.")

print('Test for t = [1]. Expect an error')
t = [1]
print(chop(t))

print('Test for t = 1. Expect an error.')
print(chop(1))

print("Test for t = ['apple','orange','banana']")
t = ['apple', 'orange', 'banana']
print('Function returns', chop(t))
print('Variable t is now', t)

print('Test for t = [1,3,2,5,4].')
t = [1, 3, 2, 5, 4]
print('Function returns', chop(t))
print('Variable t is now', t)
